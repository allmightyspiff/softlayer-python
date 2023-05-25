from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Vlan_Firewall(Entity):
    """The SoftLayer_Network_Vlan_Firewall data type contains general information relating to a single SoftLayer
VLAN firewall. This is the object which ties the running rules to a specific downstream server. Use the
[[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the
[[SoftLayer Network Firewall Update Request]] service to submit a firewall update request."""
    administrativeBypassFlag: str
    customerManagedFlag: bool
    id_: int
    primaryIpAddress: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Vlan_Firewall'

    def approveBypassRequest(self, identifier: int) -> None:
        """Approve a request from technical support to bypass the firewall."""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'approveBypassRequest', id=identifier)
        return data

    def getFirewallFirmwareVersion(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getFirewallFirmwareVersion', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Vlan_Firewall':
        """Retrieve a SoftLayer_Network_Vlan_Firewall record."""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall import Network_Vlan_Firewall
        return data

    def hasActiveTransactions(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'hasActiveTransactions', id=identifier)
        return data

    def isAccountAllowed(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'isAccountAllowed', id=identifier)
        return data

    def isHighAvailabilityUpgradeAvailable(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'isHighAvailabilityUpgradeAvailable', id=identifier)
        return data

    def rejectBypassRequest(self, identifier: int) -> None:
        """Reject a request from technical support to bypass the firewall."""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'rejectBypassRequest', id=identifier)
        return data

    def restoreDefaults(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Reset the FSA 10G firewall to factory settings."""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'restoreDefaults', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'setTags', tags, id=identifier)
        return data

    def updateRouteBypass(self, identifier: int, bypass: bool) -> 'Provisioning_Version1_Transaction':
        """Enable or disable route bypass."""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'updateRouteBypass', bypass, id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAccountId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getAccountId', id=identifier)
        return data

    def getBandwidthAllocation(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBandwidthAllocation', id=identifier)
        return data

    def getBillingCycleBandwidthUsage(self, identifier: int) -> list['Network_Bandwidth_Usage']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBillingCycleBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePrivateBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBillingCyclePrivateBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePublicBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBillingCyclePublicBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getBypassRequestStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getBypassRequestStatus', id=identifier)
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getFirewallType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getFirewallType', id=identifier)
        return data

    def getFullyQualifiedDomainName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getFullyQualifiedDomainName', id=identifier)
        return data

    def getManagementCredentials(self, identifier: int) -> 'Software_Component_Password':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getManagementCredentials', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getMetricTrackingObjectId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getMetricTrackingObjectId', id=identifier)
        return data

    def getNetworkFirewallUpdateRequests(self, identifier: int) -> list['Network_Firewall_Update_Request']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getNetworkFirewallUpdateRequests', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data

    def getNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getRules(self, identifier: int) -> list['Network_Vlan_Firewall_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall_Rule import Network_Vlan_Firewall_Rule
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getUpgradeRequest(self, identifier: int) -> 'Product_Upgrade_Request':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan_Firewall', 'getUpgradeRequest', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request import Product_Upgrade_Request
        return data
