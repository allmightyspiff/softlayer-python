from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_MassDataMigration_Request(Entity):
    """The SoftLayer_Network_Storage_MassDataMigration_Request data type contains information on a single Mass Data
Migration request. Creation of these requests is limited to SoftLayer customers through the SoftLayer
Customer Portal."""
    accountId: int
    addressId: int
    createUserId: int
    endDate: datetime
    id_: int
    modifyUserId: int
    name: str
    startDate: datetime
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_MassDataMigration_Request'

    def getAllObjects(self) -> list['Network_Storage_MassDataMigration_Request']:
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getAllObjects')
        return data

    def getAllRequestStatuses(self) -> list['Network_Storage_MassDataMigration_Request_Status']:
        """Retrieves a list of all the possible statuses"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getAllRequestStatuses')
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request_Status import Network_Storage_MassDataMigration_Request_Status
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request':
        """Retrieve a SoftLayer_Network_Storage_MassDataMigration_Request record."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getObject', id=identifier)
        return data

    def getPendingRequests(self) -> list['Network_Storage_MassDataMigration_Request']:
        """Returns placeholder MDMS requests for any MDMS order pending approval."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getPendingRequests')
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getActiveTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getAddress(self, identifier: int) -> 'Account_Address':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getAddress', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCreateEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getCreateEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getDeviceConfiguration(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request_DeviceConfiguration':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getDeviceConfiguration', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request_DeviceConfiguration import Network_Storage_MassDataMigration_Request_DeviceConfiguration
        return data

    def getDeviceModel(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getDeviceModel', id=identifier)
        return data

    def getKeyContacts(self, identifier: int) -> list['Network_Storage_MassDataMigration_Request_KeyContact']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getKeyContacts', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request_KeyContact import Network_Storage_MassDataMigration_Request_KeyContact
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getShipments(self, identifier: int) -> list['Account_Shipment']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getShipments', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data

    def getStatus(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request_Status import Network_Storage_MassDataMigration_Request_Status
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request', 'getTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data
