#!python

import click
# from prettytable import PrettyTable
import json
import requests
import os
import shutil
from string import Template
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

class SLDNgenerator():

    def __init__(self):
        cwd = os.getcwd()
        if not cwd.endswith(BASE_DIR):
            raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")
        # Make sure required directories exist
        if not os.path.isdir(f'{cwd}/sltypes'):
            os.mkdir(f'{cwd}/sltypes')
        self.metajson = None

    def getMetadata(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"{url} returned \n{response.text}\nHTTP CODE: {response.status_code}")

        self.metajson = response.json()
        return self.metajson

    def getLocalMetadata(self, filename='tools/sldn_metadata.json'):
        with open(filename, "r", encoding="utf-8") as f:
            metadata = f.read()
        self.metajson = json.loads(metadata)
        return self.metajson

    def saveMetadata(self, filename='tools/sldn_metadata.json'):
        print(f"Writing SLDN Metadata to {filename}")
        with open(filename, 'w') as f:
            json.dump(self.metajson, f, indent=4)


    def finalTouches(self):
        # SoftLayer_Entity needs a special modification
        with open(f"SoftLayer/sltypes/Entity/__init__.py", "w", encoding="utf-8") as f:
            f.write(SOFTLAYER_ENTITY)

    def generateMarkdown(self):
        for serviceName, service in self.metajson.items():
            print(f"Working on: {serviceName}")
            # noservice means datatype only.
            if service.get('noservice', False):
                self.writeDatatypeMarkdown(service)
            else:
                self.writeServiceMarkdown(service)
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

    def writeServiceMarkdown(self, serviceJson):
        # The full SLDN Name, like 'SoftLayer_Virtual_Guest'
        service_name = serviceJson.get('name')
        # Split out each part like ['SoftLayer', 'Virtual', 'Guest']
        service_parts = service_name.split('_')
        # Will become ./sltypes/SoftLayer_Virtual_Guest
        service_dir = f"./SoftLayer/sltypes/{service_name}"
        # Remove SoftLayer Prefix -> ./sltypes/Virtual_Guest
        service_dir = service_dir.replace("SoftLayer_", "")
        # Replace _ with / -> ./sltypes/Virtual/Guest
        service_dir = service_dir.replace("_", "/")
        
        # Remove the very last part -> ./sltypes/Virtual/  
        # service_dir = service_dir.replace(service_parts[-1], "")


        if not (os.path.isdir(service_dir)):
            os.makedirs(service_dir, exist_ok=True)
        template = Template(SERVICEDEF)
        
        documentation = serviceJson.get('serviceDoc', '')
        method_definitions  = []

        for methodName, method in serviceJson.get('methods', {}).items():
            method_definitions.append(self.writeMethodMarkdown(method, serviceName=service_name))
        substitions = {
            'serviceName': serviceJson.get('name'),
            'serviceType': service_parts[1],
            'layoutType' : 'service',
            'mainService': serviceJson.get('name'),
            'methods': '\n'.join(method_definitions),
            'baseClass': serviceJson.get('base', 'SoftLayer_Entity')
        }
        with open(f"{service_dir}/__init__.py", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))
        # with open(f"{service_dir}/{service_parts[-1]}.py", "w", encoding="utf-8") as f:
        #     f.write(template.substitute(substitions))
        
    def writeDatatypeMarkdown(self, serviceJson):
        # The full SLDN Name, like 'SoftLayer_Virtual_Guest'
        service_name = serviceJson.get('name')
        # Split out each part like ['SoftLayer', 'Virtual', 'Guest']
        service_parts = service_name.split('_')
        # Will become ./sltypes/SoftLayer_Virtual_Guest
        service_dir = f"./SoftLayer/sltypes/{service_name}"
        # Remove SoftLayer Prefix -> ./sltypes/Virtual_Guest
        service_dir = service_dir.replace("SoftLayer_", "")
        # Replace _ with / -> ./sltypes/Virtual/Guest
        service_dir = service_dir.replace("_", "/")
        # service_dir = service_dir.lower()

        if not (os.path.isdir(service_dir)):
            os.makedirs(service_dir, exist_ok=True)
        template = Template(DATATYPEDEF)

        substitions = {
            'dataType': service_parts[-1],
            'baseClass': serviceJson.get('base', 'SoftLayer_Entity')
        }
        with open(f"{service_dir}/__init__.py", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))

    def writeMethodMarkdown(self, json, serviceName):
        template = Template(METHODDEF)
        returnType = json.get('type', '')
        if json.get('typeArray'):
            returnType = f"list[{returnType}]"
        parameters = []
        call_args = []

        for param in json.get('parameters', []):
            param_type = self.typeCheck(param.get('type'))
            parameters.append(f"{param.get('name')}: {param_type}")
            call_args.append(f"{param.get('name')}")
        if not json.get('static', False):
            parameters.append("identifier: int")
            call_args.append("id=identifier")
        if json.get('maskable'):
            parameters.append("objectMask: Optional[str] = None")
            call_args.append("mask=objectMask")
        if json.get('filterable'):
            parameters.append("objectFilter: Optional[dict] = None")
            call_args.append("filter=objectFilter")
        if json.get('limitable'):
            parameters.append("limit: Optional[int] = None")
            call_args.append("limit=limit")
            parameters.append("offset: Optional[int] = None")
            call_args.append("offset=offset")

        substitions = {
            'methodName': json.get('name'),
            'arguments': ',\n        '.join(parameters),
            'call_args': ',\n            '.join(call_args),
            'importPath': self.getImportPath(json.get('type', '')),
            'returnStatement': self.getReturnStatement(json.get('type', '')),
            'returnType': returnType
        }
        return template.substitute(substitions)

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




@click.command()
@click.option('--download', default=False, is_flag=True)
@click.option('--clean', default=False, is_flag=True, help="Removes the sltypes so they can be built from scratch")
def main(download, clean):
    cwd = os.getcwd()
    if not cwd.endswith(BASE_DIR):
        raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")

    if clean:
        print(f"Removing {cwd}/SoftLayer/sltypes")
        try:
            shutil.rmtree(f'{cwd}/SoftLayer/sltypes')
        except FileNotFoundError:
            print("Directory doesnt exist...")

    generator = SLDNgenerator()
    if download:
        try:
            metajson = generator.getMetadata(url = METAURL)
            generator.saveMetadata()
        except Exception as e:
            print("========== ERROR ==========")
            print(f"{e}")
            print("========== ERROR ==========")
    else:
        metajson = generator.getLocalMetadata()
    jsonString = json.dumps(metajson)
    # print(jsonString)
    generator.metajson = json.loads(jsonString)
    # generator.addInChildMethods()
    generator.addInORMMethods()
    generator.saveMetadata()
    print("Generating Markdown....")
    # print(metajson)
    generator.generateMarkdown()


if __name__ == "__main__":
    main()