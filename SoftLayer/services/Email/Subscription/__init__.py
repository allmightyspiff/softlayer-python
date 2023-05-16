# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Email_Subscription(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Email_Subscription'
        self.client = client

    def disable(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disable',
            id=identifier
        )
        
        return data


    def enable(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enable',
            id=identifier
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Email_Subscription]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Email.Subscription import Subscription
        return Subscription(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Email_Subscription':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Email.Subscription import Subscription
        return Subscription(data)


    def getEnabled(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getEnabled',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


