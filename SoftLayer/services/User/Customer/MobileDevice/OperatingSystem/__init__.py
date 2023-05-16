# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_MobileDevice_OperatingSystem(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_MobileDevice_OperatingSystem'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_User_Customer_MobileDevice_OperatingSystem]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice_OperatingSystem':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


