# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Policy_Assignment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Policy_Assignment'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Assignment(data)

# This file was automatically generated with tools/generateTypes.py
    def getPolicyDocumentContents(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPolicyDocumentContents',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)


