# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Utility_Network(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Utility_Network'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def nsLookup(
        self,
        address: str,
        type: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'nsLookup',
            address,
            type
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def whois(
        self,
        address: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'whois',
            address
        )
        
        return data


