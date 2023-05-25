from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Blade(Entity):
    createDate: datetime
    disabled: int
    hardwareChildId: int
    hardwareParentId: int
    id_: int
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Blade'

    def getObject(self, identifier: int) -> 'Hardware_Blade':
        """Retrieve a SoftLayer_Hardware_Blade record."""
        data = self.client.call('SoftLayer_Hardware_Blade', 'getObject', id=identifier)
        from SoftLayer.sltypes.Hardware_Blade import Hardware_Blade
        return data

    def getHardwareChild(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware_Blade', 'getHardwareChild', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareParent(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware_Blade', 'getHardwareParent', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data
