# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class BluePages_Search(object):

    def __init__(self, client: Client) -> None:
        self.service = 'BluePages_Search'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def findBluePagesProfile(
        self,
        emailAddress: str
    ) -> 'BluePages_Container_EmployeeProfile':
        data = self.client.call(
            self.service,
            'findBluePagesProfile',
            emailAddress
        )
        
        return data


