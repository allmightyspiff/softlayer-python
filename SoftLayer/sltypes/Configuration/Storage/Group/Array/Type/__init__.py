from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Storage_Group_Array_Type(Entity):
    """Supported hardware raid modes"""
    description: str
    driveMultiplier: int
    hotspareAllow: bool
    id_: int
    keyName: str
    maximumDrives: int
    minimumDrives: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Storage_Group_Array_Type'

    def getAllObjects(self) -> list['Configuration_Storage_Group_Array_Type']:
        data = self.client.call('SoftLayer_Configuration_Storage_Group_Array_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Configuration_Storage_Group_Array_Type':
        """Retrieve a SoftLayer_Configuration_Storage_Group_Array_Type record."""
        data = self.client.call('SoftLayer_Configuration_Storage_Group_Array_Type', 'getObject', id=identifier)
        return data

    def getHardwareComponentModels(self, identifier: int) -> list['Hardware_Component_Model']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Storage_Group_Array_Type', 'getHardwareComponentModels', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model import Hardware_Component_Model
        return data
