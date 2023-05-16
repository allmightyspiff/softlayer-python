# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_External_Binding_Vendor(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_External_Binding_Vendor'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_User_External_Binding_Vendor]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Vendor import Vendor
        return Vendor(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_External_Binding_Vendor':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Vendor import Vendor
        return Vendor(data)


