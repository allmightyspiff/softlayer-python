# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_ApiAuthentication(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_ApiAuthentication'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_User_Customer_ApiAuthentication,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_ApiAuthentication':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return SL_ApiAuthentication(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_ApiAuthentication':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return SL_ApiAuthentication(data)

# This file was automatically generated with tools/generateTypes.py
    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


