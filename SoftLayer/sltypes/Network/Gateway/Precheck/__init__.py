from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_Precheck(Entity):
    category: str
    gatewayReadinessValue: str
    memberId: int
    memberReadinessValue: str
    returnCode: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_Precheck'

    def getObject(self, identifier: int) -> 'Network_Gateway_Precheck':
        """Retrieve a SoftLayer_Network_Gateway_Precheck record."""
        data = self.client.call('SoftLayer_Network_Gateway_Precheck', 'getObject', id=identifier)
        return data

    def getPrecheckStatus(self, gatewayId: int, getRollbackPrecheck: bool) -> list['Network_Gateway_Precheck']:
        """Get Precheck status for Gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Precheck', 'getPrecheckStatus', gatewayId, getRollbackPrecheck)
        return data

    def licenseManagementPrecheck(self, gatewayId: int) -> bool:
        """License Management Gateway Precheck"""
        data = self.client.call('SoftLayer_Network_Gateway_Precheck', 'licenseManagementPrecheck', gatewayId)
        return data

    def osReloadPrecheck(self, gatewayId: int) -> bool:
        """OS Reload Gateway Precheck"""
        data = self.client.call('SoftLayer_Network_Gateway_Precheck', 'osReloadPrecheck', gatewayId)
        return data

    def upgradePrecheck(self, gatewayId: int) -> bool:
        """Upgrade Gateway Precheck"""
        data = self.client.call('SoftLayer_Network_Gateway_Precheck', 'upgradePrecheck', gatewayId)
        return data
