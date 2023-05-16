# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Maintenance_Ticket(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Maintenance_Ticket'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Ticket':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Ticket import Ticket
        return Ticket(data)


    def getAvailableSlots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Slots':

        data = self.client.call(
            self.service,
            'getAvailableSlots',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Slots import Slots
        return Slots(data)


    def getMaintenanceClass(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Classification':

        data = self.client.call(
            self.service,
            'getMaintenanceClass',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification import Classification
        return Classification(data)


    def getTicket(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':

        data = self.client.call(
            self.service,
            'getTicket',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


