from SoftLayer.sltypes.Container.Tax.Rates import Container_Tax_Rates
from SoftLayer.sltypes.Entity import Entity

class Container_Tax_Cache_Item(Entity):
    """This represents one order item in a tax calculation."""
    categoryCode: str
    containerHash: str
    itemPriceId: int
    taxRates: Container_Tax_Rates
