from SoftLayer.sltypes.Network.LBaaS.LoadBalancerServerInstanceInfo import Network_LBaaS_LoadBalancerServerInstanceInfo
from SoftLayer.sltypes.Network.Subnet import Network_Subnet
from SoftLayer.sltypes.Network.LBaaS.LoadBalancerProtocolConfiguration import Network_LBaaS_LoadBalancerProtocolConfiguration
from SoftLayer.sltypes.Network.LBaaS.LoadBalancerHealthMonitorConfiguration import Network_LBaaS_LoadBalancerHealthMonitorConfiguration
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_LoadBalancer_AsAService(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order for a Load Balancer as a Service."""
    description: str
    healthMonitorConfigurations: list[Network_LBaaS_LoadBalancerHealthMonitorConfiguration]
    isPublic: bool
    name: str
    protocolConfigurations: list[Network_LBaaS_LoadBalancerProtocolConfiguration]
    publicSubnets: list[Network_Subnet]
    serverInstancesInformation: list[Network_LBaaS_LoadBalancerServerInstanceInfo]
    subnets: list[Network_Subnet]
    type_: int
    useSystemPublicIpPool: bool
