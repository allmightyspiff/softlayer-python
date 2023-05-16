# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_DedicatedHost(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_DedicatedHost'
        self.client = client

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
        templateObject: SoftLayer_Virtual_DedicatedHost
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAvailableRouters(
        self,
        dedicatedHost: SoftLayer_Virtual_DedicatedHost,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAvailableRouters',
            dedicatedHost,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_DedicatedHost':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def setTags(
        self,
        tags: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setTags',
            tags
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


    def getAllocationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Virtual_DedicatedHost_AllocationStatus':

        data = self.client.call(
            self.service,
            'getAllocationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Virtual.DedicatedHost.AllocationStatus import AllocationStatus
        return AllocationStatus(data)


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


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Virtual_DedicatedHost':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


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


    def getGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getInternalTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getInternalTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getPciDeviceAllocationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus':

        data = self.client.call(
            self.service,
            'getPciDeviceAllocationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Virtual.DedicatedHost.Pci.Device.AllocationStatus import AllocationStatus
        return AllocationStatus(data)


    def getPciDevices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Host_PciDevice]':

        data = self.client.call(
            self.service,
            'getPciDevices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Host.PciDevice import PciDevice
        return PciDevice(data)


    def getTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


