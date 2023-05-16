# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Shipment_Item(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Shipment_Item'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Account_Shipment_Item
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment_Item':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getShipment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment':
        data = self.client.call(
            self.service,
            'getShipment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment import Shipment
        return SL_Shipment(data)

# This file was automatically generated with tools/generateTypes.py
    def getShipmentItemType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment_Item_Type':
        data = self.client.call(
            self.service,
            'getShipmentItemType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Item.Type import Type
        return SL_Type(data)


