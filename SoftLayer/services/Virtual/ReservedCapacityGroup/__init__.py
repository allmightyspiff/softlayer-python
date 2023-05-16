# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_ReservedCapacityGroup(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_ReservedCapacityGroup'
        self.client = client

    def editObject(
        self,
        templateObject: 'SoftLayer_Virtual_ReservedCapacityGroup',
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
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


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


    def getAvailableInstances(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getAvailableInstances',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getBackendRouter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Router_Backend':

        data = self.client.call(
            self.service,
            'getBackendRouter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Router.Backend import Backend
        return Backend(data)


    def getInstances(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getInstances',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getInstancesCount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getInstancesCount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOccupiedInstances(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getOccupiedInstances',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


