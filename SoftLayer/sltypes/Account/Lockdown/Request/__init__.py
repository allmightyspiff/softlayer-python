from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Lockdown_Request(Entity):
    """The SoftLayer_Account_Lockdown_Request data type holds information on API requests from brand customers."""
    accountId: int
    action: str
    createDate: datetime
    id_: int
    modifyDate: datetime
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Lockdown_Request'

    def cancelRequest(self, identifier: int) -> None:
        """Allows approved brands to cancel a previously scheduled lockdown request."""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'cancelRequest', id=identifier)
        return data

    def disableLockedAccount(self, identifier: int, disableDate: str) -> int:
        """Disabling an account is a PERMANENT action. All billable items associated"""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'disableLockedAccount', disableDate, id=identifier)
        return data

    def disconnectCompute(self, accountId: int, disconnectDate: str) -> int:
        """Disconnecting a customer will disable all hardware resources (servers and"""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'disconnectCompute', accountId, disconnectDate)
        return data

    def getAccountHistory(self, accountId: int) -> list['Account_Lockdown_Request']:
        """Provides a history of an account's lockdown requests and their status."""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'getAccountHistory', accountId)
        return data

    def getObject(self, identifier: int) -> 'Account_Lockdown_Request':
        """Retrieve a SoftLayer_Account_Lockdown_Request record."""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'getObject', id=identifier)
        return data

    def reconnectCompute(self, identifier: int, reconnectDate: str) -> int:
        """Reconnecting a customer will reconnect all previously disconnected"""
        data = self.client.call('SoftLayer_Account_Lockdown_Request', 'reconnectCompute', reconnectDate, id=identifier)
        return data
