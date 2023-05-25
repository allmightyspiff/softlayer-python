from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment_Item(Entity):
    """The SoftLayer_Account_Shipment_Item data type contains information relating to a shipment's item. Basic
information such as addresses, the shipment courier, and any tracking information for as shipment is
accessible with this data type."""
    createDate: datetime
    description: str
    id_: int
    packageId: int
    shipmentId: int
    shipmentItemId: int
    shipmentItemTypeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment_Item'

    def editObject(self, identifier: int, templateObject: 'Account_Shipment_Item') -> bool:
        """Edit a shipment record."""
        data = self.client.call('SoftLayer_Account_Shipment_Item', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Shipment_Item':
        """Retrieve a SoftLayer_Account_Shipment_Item record."""
        data = self.client.call('SoftLayer_Account_Shipment_Item', 'getObject', id=identifier)
        return data

    def getShipment(self, identifier: int) -> 'Account_Shipment':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Item', 'getShipment', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data

    def getShipmentItemType(self, identifier: int) -> 'Account_Shipment_Item_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment_Item', 'getShipmentItemType', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Item_Type import Account_Shipment_Item_Type
        return data
