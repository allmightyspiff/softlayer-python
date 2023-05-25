from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment_Tracking_Data(Entity):
    """The SoftLayer_Account_Shipment_Tracking_Data data type contains information on a single piece of tracking
information pertaining to a shipment. This tracking information tracking numbers by which the shipment may be
tracked through the shipping courier."""
    createUserId: int
    id_: int
    modifyUserId: int
    packageId: int
    sequence: int
    shipmentId: int
    trackingData: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment_Tracking_Data'

    def createObject(self, templateObject: 'Account_Shipment_Tracking_Data') -> 'Account_Shipment_Tracking_Data':
        """Create a new shipment tracking data."""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Account_Shipment_Tracking_Data') -> list['Account_Shipment_Tracking_Data']:
        """Create multiple tracking data records."""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a shipment tracking datum (number)"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Shipment_Tracking_Data') -> bool:
        """Edit a tracking data."""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Shipment_Tracking_Data':
        """Retrieve a SoftLayer_Account_Shipment_Tracking_Data record."""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getObject', id=identifier)
        return data

    def getCreateEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getCreateEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getShipment(self, identifier: int) -> 'Account_Shipment':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Tracking_Data', 'getShipment', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data
