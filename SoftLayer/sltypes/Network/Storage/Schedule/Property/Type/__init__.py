from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Schedule_Property_Type(Entity):
    """A schedule property type is used to allow for a standardized method of defining network storage schedules."""
    description: str
    id_: int
    keyname: str
    name: str
    nasType: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Schedule_Property_Type'

    def getAllObjects(self) -> list['Network_Storage_Schedule_Property_Type']:
        """Returns all network storage schedule property types"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule_Property_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Schedule_Property_Type':
        """Retrieve a SoftLayer_Network_Storage_Schedule_Property_Type record."""
        data = self.client.call('SoftLayer_Network_Storage_Schedule_Property_Type', 'getObject', id=identifier)
        return data
