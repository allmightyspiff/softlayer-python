from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Component_Partition_OperatingSystem(Entity):
    """The SoftLayer_Hardware_Component_Partition_OperatingSystem data type contains general information relating to
a single SoftLayer Operating System Partition Template."""
    description: str
    id_: int
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Component_Partition_OperatingSystem'

    def getAllObjects(self) -> list['Hardware_Component_Partition_OperatingSystem']:
        data = self.client.call('SoftLayer_Hardware_Component_Partition_OperatingSystem', 'getAllObjects')
        return data

    def getByDescription(self, description: str) -> 'Hardware_Component_Partition_OperatingSystem':
        """Retrieves a list of all partition templates that match a certain description."""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_OperatingSystem', 'getByDescription', description)
        return data

    def getObject(self, identifier: int) -> 'Hardware_Component_Partition_OperatingSystem':
        """Retrieve a SoftLayer_Hardware_Component_Partition_OperatingSystem record."""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_OperatingSystem', 'getObject', id=identifier)
        return data

    def getPartitionTemplates(self, identifier: int) -> list['Hardware_Component_Partition_Template']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_OperatingSystem', 'getPartitionTemplates', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Partition_Template import Hardware_Component_Partition_Template
        return data
