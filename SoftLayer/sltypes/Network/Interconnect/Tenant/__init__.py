from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Interconnect_Tenant(Entity):
    accountId: int
    bgpAsn: int
    createDate: datetime
    errorMessage: str
    globalRoutingFlag: bool
    id_: int
    interconnectType: str
    linkSpeed: int
    localIpAddress: str
    location: str
    modifyDate: datetime
    name: str
    newGlobalRoutingFlag: bool
    newLinkSpeed: int
    note: str
    peerLinkSpeed: int
    port: str
    provider: str
    providerAccountId: int
    redundancyFlag: bool
    remoteIpAddress: str
    serviceKey: str
    serviceTypeId: int
    status: str
    vlanId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Interconnect_Tenant'

    def allowDeleteConnection(self, serviceKey: str) -> bool:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'allowDeleteConnection', serviceKey)
        return data

    def createConnection(self, templateObject: 'Network_Interconnect_Tenant') -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'createConnection', templateObject)
        return data

    def deleteConnection(self, receivedObject: 'Network_Interconnect_Tenant') -> bool:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'deleteConnection', receivedObject)
        return data

    def editConnection(self, receivedObject: 'Network_Interconnect_Tenant') -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'editConnection', receivedObject)
        return data

    def getAllConnections(self) -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getAllConnections')
        return data

    def getAllObjects(self) -> list['Network_Interconnect_Tenant']:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getAllObjects')
        from SoftLayer.sltypes.Network_Interconnect_Tenant import Network_Interconnect_Tenant
        return data

    def getAllPortLabelsWithCurrentUsage(self, directLinkLocationId: int) -> list[str]:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getAllPortLabelsWithCurrentUsage', directLinkLocationId)
        return data

    def getBgpIpRange(self) -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getBgpIpRange')
        return data

    def getConnection(self, serviceKey: str, provider: str) -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getConnection', serviceKey, provider)
        return data

    def getDirectLinkSpeeds(self, offeringType: str) -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getDirectLinkSpeeds', offeringType)
        return data

    def getNetworkZones(self) -> list[str]:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getNetworkZones')
        return data

    def getObject(self, identifier: int) -> 'Network_Interconnect_Tenant':
        """Retrieve a SoftLayer_Network_Interconnect_Tenant record."""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Interconnect_Tenant import Network_Interconnect_Tenant
        return data

    def getPorts(self, provider: str) -> str:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getPorts', provider)
        return data

    def isAdnAccount(self) -> bool:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'isAdnAccount')
        return data

    def rejectApprovalRequests(self, serviceKey: str) -> bool:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'rejectApprovalRequests', serviceKey)
        return data

    def updateConnectionStatus(self, tenantId: int) -> bool:
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'updateConnectionStatus', tenantId)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Network_Interconnect':
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Network_Interconnect import Billing_Item_Network_Interconnect
        return data

    def getDatacenterName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getDatacenterName', id=identifier)
        return data

    def getPortLabel(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getPortLabel', id=identifier)
        return data

    def getServiceType(self, identifier: int) -> 'Network_DirectLink_ServiceType':
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getServiceType', id=identifier)
        from SoftLayer.sltypes.Network_DirectLink_ServiceType import Network_DirectLink_ServiceType
        return data

    def getVendorName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getVendorName', id=identifier)
        return data

    def getZoneName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Interconnect_Tenant', 'getZoneName', id=identifier)
        return data
