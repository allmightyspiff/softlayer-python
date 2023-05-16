# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Account'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Account':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Account import Account
        return Account(data)


    def verifyCdnAccountExists(
        self,
        vendorName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'verifyCdnAccountExists',
            vendorName
        )
        
        return data


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


