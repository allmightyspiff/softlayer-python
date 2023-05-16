# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Maintenance_Window(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Maintenance_Window'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addCustomerUpgradeWindow(
        self,
        customerUpgradeWindow: SoftLayer_Container_Provisioning_Maintenance_Window
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addCustomerUpgradeWindow',
            customerUpgradeWindow
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceClassifications(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Classification]':
        data = self.client.call(
            self.service,
            'getMaintenanceClassifications',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification import Classification
        return SL_Classification(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceStartEndTime(
        self,
        ticketId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Window':
        data = self.client.call(
            self.service,
            'getMaintenanceStartEndTime',
            ticketId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Window import Window
        return SL_Window(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceWindowForTicket(
        self,
        maintenanceWindowId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Window':
        data = self.client.call(
            self.service,
            'getMaintenanceWindowForTicket',
            maintenanceWindowId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Window import Window
        return SL_Window(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceWindowTicketsByTicketId(
        self,
        ticketId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Ticket]':
        data = self.client.call(
            self.service,
            'getMaintenanceWindowTicketsByTicketId',
            ticketId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceWindows(
        self,
        beginDate: dateTime,
        endDate: dateTime,
        locationId: int,
        slotsNeeded: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Window]':
        data = self.client.call(
            self.service,
            'getMaintenanceWindows',
            beginDate,
            endDate,
            locationId,
            slotsNeeded,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Window import Window
        return SL_Window(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenceWindows(
        self,
        beginDate: dateTime,
        endDate: dateTime,
        locationId: int,
        slotsNeeded: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Window]':
        data = self.client.call(
            self.service,
            'getMaintenceWindows',
            beginDate,
            endDate,
            locationId,
            slotsNeeded,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Window import Window
        return SL_Window(data)


