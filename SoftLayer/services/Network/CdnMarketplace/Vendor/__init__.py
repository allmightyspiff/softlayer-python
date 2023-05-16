# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Vendor(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Vendor'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Vendor':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Vendor import Vendor
        return Vendor(data)


    def listVendors(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Vendor]':

        data = self.client.call(
            self.service,
            'listVendors',
            
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Vendor import Vendor
        return Vendor(data)


