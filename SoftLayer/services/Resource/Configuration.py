# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Configuration(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Configuration'
        self.client = client

    def setOsPasswordFromEncrypted(
        self,
        encryptedPassword: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setOsPasswordFromEncrypted',
            encryptedPassword
        )
        
        return data


