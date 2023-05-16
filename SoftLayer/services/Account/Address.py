# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Address(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Address'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Account_Address,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def editObject(
        self,
        templateObject: SoftLayer_Account_Address
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAllDataCenters(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Address]':

        data = self.client.call(
            self.service,
            'getAllDataCenters',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getNetworkAddress(
        self,
        name: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Address]':

        data = self.client.call(
            self.service,
            'getNetworkAddress',
            name,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


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
        return Account(data)


    def getCreateUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCreateUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getModifyEmployee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getModifyEmployee',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getModifyUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getModifyUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address.Type import Type
        return Type(data)


