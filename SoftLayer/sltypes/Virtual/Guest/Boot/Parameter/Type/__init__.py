from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Guest_Boot_Parameter_Type(Entity):
    """Describes a virtual guest boot parameter. In this the word class is used in the context of arguments sent to
cloud computing instances such as single user mode and boot into bash."""
    bootOption: str
    createDate: datetime
    description: str
    id_: int
    keyName: str
    modifyDate: datetime
    name: str
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Guest_Boot_Parameter_Type'

    def getAllObjects(self) -> list['Virtual_Guest_Boot_Parameter_Type']:
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Virtual_Guest_Boot_Parameter_Type':
        """Retrieve a SoftLayer_Virtual_Guest_Boot_Parameter_Type record."""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter_Type', 'getObject', id=identifier)
        return data
