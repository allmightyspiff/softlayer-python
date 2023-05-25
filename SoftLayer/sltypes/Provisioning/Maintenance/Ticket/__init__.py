from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Maintenance_Ticket(Entity):
    maintClassId: int
    maintWindowId: int
    maintenanceDate: datetime
    ticketId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Maintenance_Ticket'

    def getObject(self, identifier: int) -> 'Provisioning_Maintenance_Ticket':
        """Retrieve a SoftLayer_Provisioning_Maintenance_Ticket record."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Ticket', 'getObject', id=identifier)
        from SoftLayer.sltypes.Provisioning_Maintenance_Ticket import Provisioning_Maintenance_Ticket
        return data

    def getAvailableSlots(self, identifier: int) -> 'Provisioning_Maintenance_Slots':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Ticket', 'getAvailableSlots', id=identifier)
        from SoftLayer.sltypes.Provisioning_Maintenance_Slots import Provisioning_Maintenance_Slots
        return data

    def getMaintenanceClass(self, identifier: int) -> 'Provisioning_Maintenance_Classification':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Ticket', 'getMaintenanceClass', id=identifier)
        from SoftLayer.sltypes.Provisioning_Maintenance_Classification import Provisioning_Maintenance_Classification
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Ticket', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data
