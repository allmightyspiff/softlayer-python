from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Maintenance_Window(Entity):
    """The SoftLayer_Provisioning_Maintenance_Window represent a time window that SoftLayer performs a hardware or
software maintenance and upgrades."""
    beginDate: datetime
    dayOfWeek: int
    endDate: datetime
    id_: int
    locationId: int
    portalTzId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Maintenance_Window'

    def addCustomerUpgradeWindow(self, customerUpgradeWindow: 'Container_Provisioning_Maintenance_Window') -> bool:
        """Updates or creates records in the"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'addCustomerUpgradeWindow', customerUpgradeWindow)
        return data

    def getMaintenanceClassifications(self) -> list['Provisioning_Maintenance_Classification']:
        """Returns the maintenance classifications"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenanceClassifications')
        from SoftLayer.sltypes.Provisioning_Maintenance_Classification import Provisioning_Maintenance_Classification
        return data

    def getMaintenanceStartEndTime(self, ticketId: int) -> 'Provisioning_Maintenance_Window':
        """Returns a specific maintenance window"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenanceStartEndTime', ticketId)
        from SoftLayer.sltypes.Provisioning_Maintenance_Window import Provisioning_Maintenance_Window
        return data

    def getMaintenanceWindowForTicket(self, maintenanceWindowId: int) -> 'Provisioning_Maintenance_Window':
        """Returns a specific maintenance window"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenanceWindowForTicket', maintenanceWindowId)
        from SoftLayer.sltypes.Provisioning_Maintenance_Window import Provisioning_Maintenance_Window
        return data

    def getMaintenanceWindowTicketsByTicketId(self, ticketId: int) -> list['Provisioning_Maintenance_Ticket']:
        """Returns maintenance window ticket"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenanceWindowTicketsByTicketId', ticketId)
        from SoftLayer.sltypes.Provisioning_Maintenance_Ticket import Provisioning_Maintenance_Ticket
        return data

    def getMaintenanceWindows(self, beginDate: datetime, endDate: datetime, locationId: int, slotsNeeded: int) -> list['Provisioning_Maintenance_Window']:
        """Returns available maintenance windows"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenanceWindows', beginDate, endDate, locationId, slotsNeeded)
        from SoftLayer.sltypes.Provisioning_Maintenance_Window import Provisioning_Maintenance_Window
        return data

    def getMaintenceWindows(self, beginDate: datetime, endDate: datetime, locationId: int, slotsNeeded: int) -> list['Provisioning_Maintenance_Window']:
        """Returns available maintenance windows"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Window', 'getMaintenceWindows', beginDate, endDate, locationId, slotsNeeded)
        from SoftLayer.sltypes.Provisioning_Maintenance_Window import Provisioning_Maintenance_Window
        return data
