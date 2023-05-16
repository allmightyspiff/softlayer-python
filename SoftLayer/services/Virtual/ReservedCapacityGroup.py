# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_ReservedCapacityGroup(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_ReservedCapacityGroup'
        self.client = client

    def editObject(
        self,
        templateObject: SoftLayer_Virtual_ReservedCapacityGroup
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


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


    def getAvailableInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getAvailableInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getBackendRouter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Router_Backend':

        data = self.client.call(
            self.service,
            'getBackendRouter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Router.Backend import Backend
        return Backend(data)


    def getInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getInstancesCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getInstancesCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOccupiedInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup_Instance]':

        data = self.client.call(
            self.service,
            'getOccupiedInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


