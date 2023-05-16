# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Policy_Assignment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Policy_Assignment'
        self.client = client

    def acceptFromTicket(
        self,
        ticketId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'acceptFromTicket',
            ticketId,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Policy_Assignment':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Policy.Assignment import Assignment
        return Assignment(data)


    def getPolicyDocumentContents(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPolicyDocumentContents',
            id=identifier
        )
        
        return data


    def getPolicyName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPolicyName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProduct(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getProduct',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


