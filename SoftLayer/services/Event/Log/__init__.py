# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Event_Log(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Event_Log'
        self.client = client

    def getAllEventNames(
        self,
        objectName: str
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAllEventNames',
            objectName
        )
        
        return data


    def getAllEventObjectNames(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAllEventObjectNames',
            
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Event_Log]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Event.Log import Log
        return Log(data)


    def getAllUserTypes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAllUserTypes',
            
        )
        
        return data


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


