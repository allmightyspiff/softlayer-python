# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_ApiAuthentication(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_ApiAuthentication'
        self.client = client

    def editObject(
        self,
        templateObject: 'SoftLayer_User_Customer_ApiAuthentication',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_ApiAuthentication':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return ApiAuthentication(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_ApiAuthentication':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return ApiAuthentication(data)


    def getUser(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


