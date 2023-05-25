from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Maintenance_Slots(Entity):
    """The SoftLayer_Provisioning_Maintenance_Slots represent the available slots for a given maintenance window at
a SoftLayer data center."""
    availableSlots: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Maintenance_Slots'

    def getObject(self, identifier: int) -> 'Provisioning_Maintenance_Slots':
        """Retrieve a SoftLayer_Provisioning_Maintenance_Slots record."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Slots', 'getObject', id=identifier)
        return data
