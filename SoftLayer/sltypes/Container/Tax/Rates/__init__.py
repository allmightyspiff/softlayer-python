from SoftLayer.sltypes.Entity import Entity

class Container_Tax_Rates(Entity):
    """This contains the four tax rates, one for each fee type."""
    laborTaxRate: float
    locationId: float
    oneTimeTaxRate: float
    recurringTaxRate: float
    setupTaxRate: float
