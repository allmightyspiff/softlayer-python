# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Info(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Info'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Info':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Info import Info
        return SL_Info(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getAchInformation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Info_Ach]':
        data = self.client.call(
            self.service,
            'getAchInformation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Info.Ach import Ach
        return SL_Ach(data)

# This file was automatically generated with tools/generateTypes.py
    def getCurrency(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency':
        data = self.client.call(
            self.service,
            'getCurrency',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return SL_Currency(data)

# This file was automatically generated with tools/generateTypes.py
    def getCurrentBillingCycle(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Info_Cycle':
        data = self.client.call(
            self.service,
            'getCurrentBillingCycle',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Info.Cycle import Cycle
        return SL_Cycle(data)

# This file was automatically generated with tools/generateTypes.py
    def getLastBillDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':
        data = self.client.call(
            self.service,
            'getLastBillDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNextBillDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':
        data = self.client.call(
            self.service,
            'getNextBillDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


