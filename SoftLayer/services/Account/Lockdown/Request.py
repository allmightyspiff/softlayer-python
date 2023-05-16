# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Lockdown_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Lockdown_Request'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def cancelRequest(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'cancelRequest',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def disableLockedAccount(
        self,
        disableDate: str
    ) -> 'int':
        data = self.client.call(
            self.service,
            'disableLockedAccount',
            disableDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def disconnectCompute(
        self,
        accountId: int,
        disconnectDate: str
    ) -> 'int':
        data = self.client.call(
            self.service,
            'disconnectCompute',
            accountId,
            disconnectDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAccountHistory(
        self,
        accountId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Lockdown_Request]':
        data = self.client.call(
            self.service,
            'getAccountHistory',
            accountId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Lockdown.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Lockdown_Request':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Lockdown.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def reconnectCompute(
        self,
        reconnectDate: str
    ) -> 'int':
        data = self.client.call(
            self.service,
            'reconnectCompute',
            reconnectDate
        )
        
        return data


