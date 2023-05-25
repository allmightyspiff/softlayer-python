from SoftLayer.sltypes.Network.Interconnect.Tenant import Network_Interconnect_Tenant
from SoftLayer.sltypes.Network.DirectLink.Location import Network_DirectLink_Location
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Interconnect(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder when
purchasing a Network Interconnect."""
    bgpAsn: str
    interconnectId: int
    interconnectLocation: Network_DirectLink_Location
    interconnectTenant: Network_Interconnect_Tenant
    ipAddressRange: str
    name: str
    networkIdentifier: str
