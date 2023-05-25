from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Host(Entity):
    """The virtual host represents the platform on which virtual guests reside. At times a virtual host has no
allocations on the physical server, however with many modern platforms it is a virtual machine with small CPU
and Memory allocations that runs in the Control Domain."""
    accountId: int
    createDate: datetime
    description: str
    enabledFlag: int
    hardwareId: int
    id_: int
    modifyDate: datetime
    name: str
    physicalMemoryCapacity: int
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Host'

    def getObject(self, identifier: int) -> 'Virtual_Host':
        """Retrieve a SoftLayer_Virtual_Host record."""
        data = self.client.call('SoftLayer_Virtual_Host', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_Host', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getHardware(self, identifier: int) -> 'Hardware_Server':
        """"""
        data = self.client.call('SoftLayer_Virtual_Host', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware_Server import Hardware_Server
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Virtual_Host', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getPciDevices(self, identifier: int) -> list['Virtual_Host_PciDevice']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Host', 'getPciDevices', id=identifier)
        from SoftLayer.sltypes.Virtual_Host_PciDevice import Virtual_Host_PciDevice
        return data
