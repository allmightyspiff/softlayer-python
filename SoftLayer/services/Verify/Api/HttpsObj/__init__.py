# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Verify_Api_HttpsObj(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Verify_Api_HttpsObj'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Verify_Api_HttpsObj',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Verify_Api_HttpsObj':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Verify.Api.HttpsObj import HttpsObj
        return HttpsObj(data)


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


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Verify_Api_HttpsObj]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Verify.Api.HttpsObj import HttpsObj
        return HttpsObj(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Verify_Api_HttpsObj':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Verify.Api.HttpsObj import HttpsObj
        return HttpsObj(data)


