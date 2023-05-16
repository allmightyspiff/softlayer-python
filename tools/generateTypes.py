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

class $serviceName(object):

    def __init__(self, client: Client) -> None:
        self.service = '$serviceName'
        self.client = client
$methods

"""

METHODDEF = """# This file was automatically generated with tools/generateTypes.py
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
from collections import UserDict
class $dataType(UserDict):
    pass
"""

class SLDNgenerator():

    def __init__(self):
        cwd = os.getcwd()
        if not cwd.endswith(BASE_DIR):
            raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")
        # Make sure required directories exist
        if not os.path.isdir(f'{cwd}/datatypes'):
            os.mkdir(f'{cwd}/datatypes')
        if not os.path.isdir(f'{cwd}/services'):
            os.mkdir(f'{cwd}/services')
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


    def generateMarkdown(self):
        for serviceName, service in self.metajson.items():
            print(f"Working on: {serviceName}")
            # noservice means datatype only.
            if service.get('noservice', False) == False:
                self.writeServiceMarkdown(service)

            self.writeDatatypeMarkdown(service)

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
        # Will become ./services/SoftLayer_Virtual_Guest
        service_dir = f"./SoftLayer/services/{service_name}"
        # Remove SoftLayer Prefix -> ./services/Virtual_Guest
        service_dir = service_dir.replace("SoftLayer_", "")
        # Replace _ with / -> ./services/Virtual/Guest
        service_dir = service_dir.replace("_", "/")
        
        # Remove the very last part -> ./services/Virtual/  
        service_dir = service_dir.replace(service_parts[-1], "")


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
            'methods': '\n'.join(method_definitions)
        }
        with open(f"{service_dir}/{service_parts[-1]}.py", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))
        
    def writeDatatypeMarkdown(self, serviceJson):
        # The full SLDN Name, like 'SoftLayer_Virtual_Guest'
        service_name = serviceJson.get('name')
        # Split out each part like ['SoftLayer', 'Virtual', 'Guest']
        service_parts = service_name.split('_')
        # Will become ./datatypes/SoftLayer_Virtual_Guest
        service_dir = f"./SoftLayer/datatypes/{service_name}"
        # Remove SoftLayer Prefix -> ./datatypes/Virtual_Guest
        service_dir = service_dir.replace("SoftLayer_", "")
        # Replace _ with / -> ./datatypes/Virtual/Guest
        service_dir = service_dir.replace("_", "/")
        # service_dir = service_dir.lower()

        if not (os.path.isdir(service_dir)):
            os.makedirs(service_dir, exist_ok=True)
        template = Template(DATATYPEDEF)

        substitions = {
            'dataType': service_parts[-1],
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
        if json.get('static') is False:
            parameters.append("id: int")
            call_args.append("id")
        for param in json.get('parameters', []):
            param_type = self.typeCheck(param.get('type'))
            parameters.append(f"{param.get('name')}: {param_type}")
            call_args.append(f"{param.get('name')}")
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
        return f"return SL_{class_name[-1]}(data)"        

    @staticmethod
    def getImportPath(returnType: str) -> str:
        if 'SoftLayer_' not in returnType:
            return ''
        import_path = returnType.replace('SoftLayer_', '')
        import_path = import_path.replace('_', '.')
        class_name = returnType.split('_')
        return f"from SoftLayer.datatypes.{import_path} import {class_name[-1]}"

    @staticmethod
    def typeCheck(sl_type: str) -> str:
        if sl_type == 'string':
            return 'str'
        return sl_type




@click.command()
@click.option('--download', default=False, is_flag=True)
@click.option('--clean', default=False, is_flag=True, help="Removes the services and datatypes directories so they can be built from scratch")
def main(download, clean):
    cwd = os.getcwd()
    if not cwd.endswith(BASE_DIR):
        raise Exception(f"Working Directory should be {BASE_DIR}, is currently {cwd}")

    if clean:
        dirs = ['datatypes', 'services']
        for directory in dirs:
            print(f"Removing {cwd}/{directory}")
            try:
                shutil.rmtree(f'{cwd}/{directory}')
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

    # fix mediaWiki links. So far its easiest just to regex the whole JSON string
    jsonString = json.dumps(metajson)
    # print(jsonString)
    generator.metajson = json.loads(jsonString)
    generator.addInChildMethods()
    generator.addInORMMethods()
    generator.saveMetadata()
    print("Generating Markdown....")
    # print(metajson)
    generator.generateMarkdown()


if __name__ == "__main__":
    main()