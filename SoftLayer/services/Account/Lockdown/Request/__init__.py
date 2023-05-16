# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Lockdown_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Lockdown_Request'
        self.client = client

    def cancelRequest(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'cancelRequest',
            id=identifier
        )
        
        return data


    def disableLockedAccount(
        self,
        disableDate: str,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'disableLockedAccount',
            disableDate,
            id=identifier
        )
        
        return data


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
        return Request(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Lockdown_Request':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Lockdown.Request import Request
        return Request(data)


    def reconnectCompute(
        self,
        reconnectDate: str,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'reconnectCompute',
            reconnectDate,
            id=identifier
        )
        
        return data


