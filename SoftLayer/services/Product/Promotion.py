# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Promotion(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Promotion'
        self.client = client

    def findByPromoCode(
        self,
        code: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Container_Product_Promotion':

        data = self.client.call(
            self.service,
            'findByPromoCode',
            code,
            mask=objectMask
        )
        from SoftLayer.datatypes.Container.Product.Promotion import Promotion
        return Promotion(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Promotion':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Promotion import Promotion
        return Promotion(data)


