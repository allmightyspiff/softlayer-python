from SoftLayer.sltypes.Billing.Item import Billing_Item
from SoftLayer.sltypes.Billing_Item import Billing_Item

class Billing_Item_Network_Subnet(Billing_Item):
    """The SoftLayer_Billing_Item_Network_Subnet data type contains general information relating to a single
SoftLayer billing item whose item category code is one of the following:  * pri_ip_address *
static_sec_ip_addresses (static secondary) * sov_sec_ip_addresses (secondary on vlan, also known as "portable
ips") * sov_sec_ip_addresses_pub (sov_sec_ip_addresses public only) * sov_sec_ip_addresses_priv
(sov_sec_ip_addresses private only) * sec_ip_addresses (old style, secondary ip addresses)   These item
categories denote that the billing item has subnet information attached."""
    resourceName: str
    resourceTableId: int
