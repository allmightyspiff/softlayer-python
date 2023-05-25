from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_DedicatedHost(Entity):
    """This data type presents the structure for a dedicated host. The data type contains relational properties to
distinguish a dedicated host and associate an account to it."""
    accountId: int
    cpuCount: int
    createDate: datetime
    diskCapacity: int
    id_: int
    memoryCapacity: int
    modifyDate: datetime
    name: str
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_DedicatedHost'

    def deleteObject(self, identifier: int) -> bool:
        """Reclaim a dedicated host to cancel it's use."""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Virtual_DedicatedHost') -> bool:
        """Edit a dedicated host's properties."""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'editObject', templateObject, id=identifier)
        return data

    def getAvailableRouters(self, dedicatedHost: 'Virtual_DedicatedHost') -> list['Hardware']:
        """Get available backend routers in a datacenter to order a dedicated host."""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getAvailableRouters', dedicatedHost)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getObject(self, identifier: int) -> 'Virtual_DedicatedHost':
        """Retrieve a SoftLayer_Virtual_DedicatedHost record."""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getObject', id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'setTags', tags, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAllocationStatus(self, identifier: int) -> 'Container_Virtual_DedicatedHost_AllocationStatus':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getAllocationStatus', id=identifier)
        from SoftLayer.sltypes.Container_Virtual_DedicatedHost_AllocationStatus import Container_Virtual_DedicatedHost_AllocationStatus
        return data

    def getBackendRouter(self, identifier: int) -> 'Hardware_Router_Backend':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getBackendRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router_Backend import Hardware_Router_Backend
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Virtual_DedicatedHost':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Virtual_DedicatedHost import Billing_Item_Virtual_DedicatedHost
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getInternalTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getInternalTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getPciDeviceAllocationStatus(self, identifier: int) -> 'Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus':
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getPciDeviceAllocationStatus', id=identifier)
        from SoftLayer.sltypes.Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus import Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus
        return data

    def getPciDevices(self, identifier: int) -> list['Virtual_Host_PciDevice']:
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getPciDevices', id=identifier)
        from SoftLayer.sltypes.Virtual_Host_PciDevice import Virtual_Host_PciDevice
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Virtual_DedicatedHost', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data
