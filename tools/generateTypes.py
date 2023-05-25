#!python

import click
import ast
import builtins
import keyword
import pathlib

import textwrap
# from prettytable import PrettyTable
import json
import requests
import os
import shutil
from string import Template
from typing import Optional
import re


METAURL = 'https://api.softlayer.com/metadata/v3.1'
BASE_DIR = 'softlayer-python'

SERVICEDEF = """# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional
$extraImports

class $serviceName($baseClass):

    def __init__(self, client: Client) -> None:
        self.service = '$serviceName'
        self.client = client
$methods

"""

METHODDEF = """
    def $methodName(
        self,
        $arguments
    ) -> '$returnType':

        data = self.client.call(
            self.service,
            '$methodName',
            $call_args
        )
        $importPath
        $returnStatement
"""

DATATYPEDEF = """# This file was automatically generated with tools/generateTypes.py
class $dataType($baseClass):
    pass
"""

SOFTLAYER_ENTITY = """# This file was automatically generated with tools/generateTypes.py
from collections import UserDict
class SoftLayer_Entity(UserDict):
    pass
"""

def doc_text_ast(doc: str) -> ast.Expr:
    return ast.Expr(ast.Constant("\n".join(textwrap.wrap(doc.strip(), width=109))))

def get_property_name(name: str) -> str:
    if keyword.iskeyword(name):
        print(f"{name} IS A KEYWORD!!!")
        name += "_"
    builtin_names = [name for name, val in builtins.__dict__.items()]
    if name in builtin_names:
        print(f"{name} IS A BUILTIN!!!")
        name += "_"
    return name


class SLDNgenerator():

    def __init__(self, metaurl=None):
        cwd = os.getcwd()
        if not metaurl:
            metaurl = METAURL
        if not cwd.endswith(BASE_DIR):
            raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")
        # Make sure required directories exist
        self.typesDir = os.path.join(cwd, 'SoftLayer/sltypes')
        if not os.path.isdir(self.typesDir):
            print(f"Creating {self.typesDir}")
            os.mkdir(self.typesDir)
        self.metaurl = metaurl
        self.metajson = None

    def getMetadata(self):
        """Gets metadata from a live url, default to https://api.softlayer.com/metadata/v3.1"""
        response = requests.get(self.metaurl)
        if response.status_code != 200:
            raise Exception(f"{url} returned \n{response.text}\nHTTP CODE: {response.status_code}")

        self.metajson = response.json()
        # self.addInChildMethods()
        self.addInORMMethods()
        self.saveMetadata()

        return self.metajson

    def getLocalMetadata(self, filename='tools/sldn_metadata.json'):
        """loads metadata from local tools/sldn_metadata.json file"""
        with open(filename, "r", encoding="utf-8") as f:
            metadata = f.read()
        self.metajson = json.loads(metadata)
        return self.metajson

    def saveMetadata(self, filename='tools/sldn_metadata.json'):
        """updates tools/sldn_metadata.json with updated metadata"""
        print(f"Writing SLDN Metadata to {filename}")
        with open(filename, 'w') as f:
            json.dump(self.metajson, f, indent=4)

    def clean(self):
        """Removes all the auto generated types"""
        print(f"Removing directory: {self.typesDir}")
        try:
            shutil.rmtree(f'{self.typesDir}')
            print(f"Creating empty directory: {self.typesDir}")
            os.mkdir(self.typesDir)
        except FileNotFoundError:
            print("Directory doesnt exist...")



    def finalTouches(self):
        # SoftLayer_Entity needs a special modification
        with open(f"SoftLayer/sltypes/Entity/__init__.py", "w", encoding="utf-8") as f:
            f.write(SOFTLAYER_ENTITY)
        # ensure modules exist for every module folder that might not have a class
        for root, dirs, files in os.walk(self.typesDir, topdown=False):
            if "__init__.py" not in files:
                fp = open(os.path.join(root, "__init__.py"), "w")
                fp.close()

    def generate(self):
        for serviceName, service in self.metajson.items():
            print(f"Working on: {serviceName}")
            skellington = ServiceAndTypeGenerator(serviceName, service)
            module_ast = skellington.get_module()
            # set up the module folders
            module_folder = os.path.join(self.typesDir, skellington.get_module_folder())
            print("module folder: " + module_folder)

            pathlib.Path(module_folder).mkdir(parents=True, exist_ok=True)

            file = os.path.join(module_folder, "__init__.py")
            src = ast.unparse(module_ast)
            # write file
            with open(file, "w") as fp:
                fp.write(src + "\n")

        self.finalTouches()

            

    def addInORMMethods(self):
        for serviceName, service in self.metajson.items():
            # noservice means datatype only.
            if service.get('noservice', False) == False:
                for propName, prop in service.get('properties', {}).items():
                    if prop.get('form', '') == 'relational':
                        # capitlize() sadly lowercases the other letters in the string
                        ormName = f"get{propName[0].upper()}{propName[1:]}"
                        ormMethod = {
                            'doc': prop.get('doc', ''),
                            'docOverview': "",
                            'name': ormName,
                            'type': prop.get('type'),
                            'typeArray': prop.get('typeArray', None),
                            'ormMethod': True,
                            'maskable': True,
                            'filterable': True,
                            'deprecated': prop.get('deprecated', False)
                        }
                        if ormMethod['typeArray']:
                            ormMethod['limitable'] = True
                        self.metajson[serviceName]['methods'][ormName] = ormMethod
        return self.metajson

    def addInChildMethods(self):
        for serviceName, service in self.metajson.items():
            self.metajson[serviceName]['methods'] = self.getBaseMethods(serviceName, 'methods')
            self.metajson[serviceName]['properties'] = self.getBaseMethods(serviceName, 'properties')


    def getBaseMethods(self, serviceName, objectType):
        """Responsible for pulling in properties or methods from the base class of the service requested"""
        service = self.metajson[serviceName]
        methods = service.get(objectType, {})
        if service.get('base', "SoftLayer_Entity") != "SoftLayer_Entity":
            
            baseMethods = self.getBaseMethods(service.get('base'), objectType)
            for bName, bMethod in baseMethods.items():
                if not methods.get(bName, False):
                    methods[bName] = bMethod
        return methods                  

    @staticmethod
    def getReturnStatement(returnType: str) -> str:
        if 'SoftLayer_' not in returnType:
            return 'return data'
        class_name = returnType.split('_')
        return f"return {class_name[-1]}(data)"        

    @staticmethod
    def getImportPath(returnType: str) -> str:
        if 'SoftLayer_' not in returnType:
            return ''
        import_path = returnType.replace('SoftLayer_', '')
        import_path = import_path.replace('_', '.')
        class_name = returnType.split('_')
        return f"from SoftLayer.sltypes.{import_path} import {class_name[-1]}"

    @staticmethod
    def typeCheck(sl_type: str) -> str:
        if sl_type == 'string':
            return 'str'
        if sl_type == 'boolean':
            return 'bool'
        if sl_type == 'dateTime':
            return 'str'
        if 'SoftLayer_' in sl_type:
            return f"'{sl_type}'"
        return sl_type



class ServiceAndTypeGenerator:
    _name: str
    _service_doc: str
    _type_doc: str
    _properties: dict
    _methods: dict
    _no_service: bool
    _base: Optional[str]
    _imports: dict
    _class_names: dict

    def __init__(self, name: str, meta: dict):
        self._name = name
        self._service_doc = meta["serviceDoc"].strip() if "serviceDoc" in meta else ""
        self._type_doc = meta["typeDoc"].strip() if "typeDoc" in meta else ""
        self._properties = meta["properties"] if "properties" in meta else {}
        self._methods = meta["methods"] if "methods" in meta else {}
        self._no_service = meta["noservice"] if "noservice" in meta else False
        self._base = meta["base"] if "base" in meta else "SoftLayer_Entity"
        # if self._name == "SoftLayer_Entity":
        #     self._base = None

        self._imports = {}
        self._class_names = {}

    def get_module_folder(self) -> str:
        name = self.normalize_name(self._name)
        # SoftLayer_Network_Vlan becomes Network/Vlan
        folder = "/".join(name.split("_"))
        return folder

    def get_module(self) -> ast.Module:
        module = ast.Module()
        module.body = []

        module.body.append(self.get_type_ast())
        if not self._no_service:
            module.body.append(self.get_service_ast())
        module.type_ignores = []

        # we looked at all the references to other types, import them and prepend
        for module_name, imports in self._imports.items():
            names = []
            for i, a in imports.items():
                if i != a:
                    names.append(ast.alias(name=i, asname=a))
                else:
                    names.append(ast.alias(name=i))
            module.body.insert(0, ast.ImportFrom(module=module_name, names=names))

        ast.fix_missing_locations(module)
        return module

    def get_service_ast(self) -> ast.ClassDef:
        class_def = ast.ClassDef(self.normalize_name(self._name))
        class_def.bases = []
        class_def.keywords = []
        class_def.body = []
        class_def.decorator_list = []

        # add service doc
        if len(self._service_doc) > 0:
            class_def.body.append(doc_text_ast(self._service_doc))

        # add __init__
        class_def.body.append(self._get_init_func())

        for method in self._methods.values():
            class_def.body.append(self.generate_method_ast(method))

        return class_def

    def _get_init_func(self) -> ast.FunctionDef:
        args = [ast.arg("self"), ast.arg("client", annotation=ast.Name('BaseClient'))]

        func = ast.FunctionDef("__init__")
        func.args = ast.arguments([], args, [], [], [], [], [])
        func.body = []
        func.decorator_list = []
        func.returns = None
        func.type_comment = None

        func.body.append(
            ast.Assign(targets=[ast.Attribute(value=ast.Name(id="self"), attr="_client")], value=ast.Name(id="client"))
        )
        func.body.append(
            ast.Assign(targets=[ast.Attribute(value=ast.Name(id="self"), attr="_name")], value=ast.Constant(self._name))
        )
        return func

    def generate_method_ast(self, method: dict) -> ast.FunctionDef:
        args = [ast.arg("self")]
        call_args = [
            ast.Name(id=f"'{self._name}'", ctx=ast.Load()),
            ast.Name(id=f"'{method['name']}'", ctx=ast.Load())
        ]
        keyed_call_args = []

        if "static" not in method or not method["static"]:
            # method is not static, so an id is required. Make it the first argument
            args.append(ast.arg("identifier", annotation=ast.Name(self.use("typing", "int"))))
            keyed_call_args.append(ast.keyword(arg='id', value=ast.arg("identifier")))

        if "parameters" in method:
            for parameter in method["parameters"]:
                args.append(
                    ast.arg(get_property_name(parameter["name"]), annotation=self.meta_type_to_ast(parameter["type"]))
                )
                call_args.append(ast.arg(arg=parameter["name"]))

        func = ast.FunctionDef(method["name"])
        # TODO Add objectmask / objectfilter / resultlimit
        func.args = ast.arguments([], args, [], [], [], [], [])
        func.body = [        ]
        func.decorator_list = []
        func.returns = self.method_type_to_ast(method)
        func.type_comment = None

        if "docOverview" in method:
            func.body.append(doc_text_ast(method["docOverview"]))

        # https://docs.python.org/3/library/ast.html#ast.Call

        func.body.append(         
            ast.Assign(
                targets=[ast.Name(id="data", ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id="self.client.call", ctx=ast.Load()),
                    args=call_args,
                    keywords=keyed_call_args
                )
            )
        )
        func.body.append(
            ast.parse(self.getReturnStatement(method['type']))
        )

        return func

    def get_type_ast(self) -> ast.ClassDef:

        class_def = ast.ClassDef(self.normalize_name(self._name))
        class_def.keywords = []
        class_def.body = []
        class_def.decorator_list = []

        class_def.bases = []
        if self._base:
            class_def.bases.append(self.meta_type_to_ast(self._base))

        if len(self._type_doc) > 0:
            class_def.body.append(doc_text_ast(self._type_doc))

        if len(self._properties) > 0:
            for prop in self._properties.values():
                class_def.body.append(self.type_property_ast(prop))

        if len(class_def.body) == 0:
            # if an empty body, add pass
            class_def.body.append(ast.Pass())

        return class_def

    def type_property_ast(self, prop: dict) -> ast.AnnAssign:
        annotation = self.meta_type_to_ast(prop["type"], for_property=True)
        if "typeArray" in prop and prop["typeArray"]:
            annotation = ast.Subscript(value=ast.Name("list"), slice=annotation)
        return ast.AnnAssign(target=ast.Name(get_property_name(prop["name"])), annotation=annotation, simple=1)

    def get_client_name(self):
        return "BaseClient"

    def method_type_to_ast(self, method: dict) -> ast.Expr:
        expr = self.meta_type_to_ast(method["type"])
        if "typeArray" in method and method["typeArray"]:
            expr = ast.Subscript(ast.Name("list"), expr)
        return expr


    def meta_type_to_ast(self, meta_type: str, for_property: bool = False) -> object:
        """
        Converts an IMS API type into a python ast expression.
        :param meta_type:
        :param for_property:
        :return:
        """
        match meta_type:
            case "void":
                return ast.Constant(value=None)
            case "boolean":
                return ast.Name("bool")
            case "int":
                return ast.Name("int")
            case "unsignedInt":
                return ast.Name("int")
            case "unsignedLong":
                return ast.Name("int")
            case "nonNegativeInteger":
                return ast.Name("int")
            case "float":
                return ast.Name("float")
            case "decimal":
                return ast.Name("float")
            case "base64Binary":
                return ast.Name("str")
            case "string":
                return ast.Name("str")
            case "json":
                return ast.Name("str")
            case "enum":
                return ast.Name("str")
            case "dateTime":
                return ast.Name(self.use("datetime", "datetime"))
            case _:
                # assume it's a type name
                (module_name, type_name) = self.meta_type_to_module_and_class(meta_type)
                if for_property and self.type_matches(module_name, type_name):
                    # type property references itself
                    return ast.Subscript(ast.Name(self.use("typing", "Optional")), ast.Name(self.use("typing", "Self")))

                return ast.Name(self.use(module_name, type_name))

    def use(self, module_name: str, type_name: str) -> str:
        """
        Handles recording importing of the given module and class name combination.
        If a type name is already in use, an alternate name is returned.
        :param module_name:
        :param type_name:
        :return:
        """
        if self.type_matches(module_name, type_name):
            # no need to import for the same module
            return type_name

        alias = type_name
        # if (type_name in self._class_names and self._class_names[type_name] != module_name) or (
        #     get_type_name(self._name) == type_name
        # ):
        #     alias = "".join(i.title() for i in module_name.split(".")) + type_name

        if module_name not in self._imports:
            self._imports[module_name] = {}
        if type_name not in self._imports[module_name]:
            self._imports[module_name][type_name] = alias
        self._class_names[alias] = module_name
        return alias

    def meta_type_to_module_and_class(self, meta_type: str) -> (str, str):
        return self.get_module_name(meta_type), self.normalize_name(meta_type)

    def type_matches(self, module_name: str, type_name: str) -> bool:
        return self.get_module_name(self._name) == module_name and self.normalize_name(self._name) == type_name



    def get_module_name(self, meta_type: str) -> str:
        name = self.normalize_name(meta_type)
        module = ".".join(name.split("_"))
        return module

    @staticmethod
    def normalize_name(name: str) -> str:
        if name.startswith("SoftLayer_"):
            return name.removeprefix("SoftLayer_")
        else:
            return name

    def getReturnStatement(self, returnType: str) -> str:
        if 'SoftLayer_' not in returnType:
            return 'return data'
        if returnType == 'void':
            return 'return None'
        return f"return {self.normalize_name(returnType)}(data)" 


@click.command()
@click.option('--download', default=False, is_flag=True)
@click.option('--clean', default=False, is_flag=True, help="Removes the sltypes so they can be built from scratch")
def main(download, clean):
    cwd = os.getcwd()
    if not cwd.endswith(BASE_DIR):
        raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")

    generator = SLDNgenerator(metaurl = METAURL)
    if download:
        try:
            metajson = generator.getMetadata()
        except Exception as e:
            print("========== ERROR DOWNLOADING METADATA ==========")
            print(f"{e}")
            print("========== ^^^^^^^ ERROR  ^^^^^^^^ ==========")
    else:
        metajson = generator.getLocalMetadata()

    if clean:
        generator.clean()

    print("Generating Markdown....")
    generator.generate()


if __name__ == "__main__":
    main()