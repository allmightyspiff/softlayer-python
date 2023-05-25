from SoftLayer.sltypes.Billing.Item import Billing_Item
from SoftLayer.sltypes.Billing_Item import Billing_Item

class Billing_Item_Virtual_Dedicated_Rack(Billing_Item):
    """A SoftLayer_Billing_Item_Virtual_Dedicated_Rack data type models the billing information for a single
bandwidth pooling. Bandwidth pooling members share their public bandwidth allocations, and incur overage
charges instead of the overages on individual rack members. Virtual rack billing items are the parent items
for all of it's rack membership billing items."""
