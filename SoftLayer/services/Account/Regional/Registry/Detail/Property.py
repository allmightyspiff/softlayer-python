# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Regional_Registry_Detail_Property(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Regional_Registry_Detail_Property'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Account_Regional_Registry_Detail_Property,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail_Property':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Property import Property
        return Property(data)


    def createObjects(
        self,
        templateObjects: SoftLayer_Account_Regional_Registry_Detail_Property,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Regional_Registry_Detail_Property]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Property import Property
        return Property(data)


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Account_Regional_Registry_Detail_Property
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_Account_Regional_Registry_Detail_Property
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail_Property':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Property import Property
        return Property(data)


    def getDetail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':

        data = self.client.call(
            self.service,
            'getDetail',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return Detail(data)


    def getPropertyType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail_Property_Type':

        data = self.client.call(
            self.service,
            'getPropertyType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail.Property.Type import Type
        return Type(data)


