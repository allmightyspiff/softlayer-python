# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Regional_Registry_Detail(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Regional_Registry_Detail'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Account_Regional_Registry_Detail',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return Detail(data)


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Account_Regional_Registry_Detail',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return Detail(data)


    def updateReferencedRegistrations(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Subnet_Registration_TransactionDetails':

        data = self.client.call(
            self.service,
            'updateReferencedRegistrations',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Subnet.Registration.TransactionDetails import TransactionDetails
        return TransactionDetails(data)


    def validatePersonForAllRegistrars(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Message]':

        data = self.client.call(
            self.service,
            'validatePersonForAllRegistrars',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Message import Message
        return Message(data)


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getDetailType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail_Type':

        data = self.client.call(
            self.service,
            'getDetailType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Type import Type
        return Type(data)


    def getDetails(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration_Details]':

        data = self.client.call(
            self.service,
            'getDetails',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Details import Details
        return Details(data)


    def getProperties(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Regional_Registry_Detail_Property]':

        data = self.client.call(
            self.service,
            'getProperties',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Property import Property
        return Property(data)


    def getRegionalInternetRegistryHandle(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Rwhois_Handle':

        data = self.client.call(
            self.service,
            'getRegionalInternetRegistryHandle',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Rwhois.Handle import Handle
        return Handle(data)


