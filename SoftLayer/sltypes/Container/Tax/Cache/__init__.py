from SoftLayer.sltypes.Container.Tax.Cache.Item import Container_Tax_Cache_Item
from SoftLayer.sltypes.Entity import Entity

class Container_Tax_Cache(Entity):
    """These are the results of a tax calculation. The tax calculation was kicked off but allowed to run in the
background. This type stores the results so that an interface can be updated with up-to-date information."""
    effectiveTaxRate: float
    failureMessage: str
    items: list[Container_Tax_Cache_Item]
    status: str
    totalTaxAmount: float
