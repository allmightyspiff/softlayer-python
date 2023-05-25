from SoftLayer.sltypes.Entity import Entity

class Product_Catalog(Entity):
    """A Catalog is defined as a set of prices for products that SoftLayer offers for sale. These prices are
organized into packages which represent the different servers and services that SoftLayer offers."""
    keyName: str
