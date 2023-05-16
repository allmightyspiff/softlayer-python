# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet_Rwhois_Data(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet_Rwhois_Data'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_Subnet_Rwhois_Data
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Rwhois_Data':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Rwhois.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)


