# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Auxiliary_Shipping_Courier_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Auxiliary_Shipping_Courier_Type'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Shipping_Courier_Type':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier.Type import Type
        return Type(data)


    def getTypeByKeyName(
        self,
        keyName: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Auxiliary_Shipping_Courier_Type':

        data = self.client.call(
            self.service,
            'getTypeByKeyName',
            keyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier.Type import Type
        return Type(data)


    def getCourier(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Auxiliary_Shipping_Courier]':

        data = self.client.call(
            self.service,
            'getCourier',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier import Courier
        return Courier(data)


