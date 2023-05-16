# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Policy_Assignment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Policy_Assignment'
        self.client = client

    def acceptFromTicket(
        self,
        ticketId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'acceptFromTicket',
            ticketId
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Policy_Assignment':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Policy.Assignment import Assignment
        return Assignment(data)


    def getPolicyDocumentContents(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPolicyDocumentContents',
            
        )
        
        return data


    def getPolicyName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPolicyName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProduct(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getProduct',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


