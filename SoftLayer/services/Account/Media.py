# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Media(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Media'
        self.client = client

    def editObject(
        self,
        templateObject: SoftLayer_Account_Media
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAllMediaTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Media_Type]':

        data = self.client.call(
            self.service,
            'getAllMediaTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Media.Type import Type
        return Type(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media import Media
        return Media(data)


    def removeMediaFromList(
        self,
        mediaTemplate: SoftLayer_Account_Media
    ) -> 'int':

        data = self.client.call(
            self.service,
            'removeMediaFromList',
            mediaTemplate
        )
        
        return data


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


    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
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


    def getRequest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media_Data_Transfer_Request':

        data = self.client.call(
            self.service,
            'getRequest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media.Data.Transfer.Request import Request
        return Request(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media.Type import Type
        return Type(data)


    def getVolume(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getVolume',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


