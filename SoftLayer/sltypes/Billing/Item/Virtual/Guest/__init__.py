from SoftLayer.sltypes.Billing.Item import Billing_Item
from SoftLayer.sltypes.Billing_Item import Billing_Item

class Billing_Item_Virtual_Guest(Billing_Item):
    """The SoftLayer_Billing_Item_Virtual_Guest data type contains general information relating to a single
SoftLayer billing item for guests."""
    resourceTableId: int
