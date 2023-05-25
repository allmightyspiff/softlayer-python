from SoftLayer.sltypes.Entity import Entity

class Billing_Order_Type(Entity):
    """The SoftLayer_Billing_Oder_Type data type contains general information relating to all the different types of
orders that exist. This data pertains only to where an order was generated from, from any of the SoftLayer
websites with ordering interfaces or directly through the SoftLayer API."""
    description: str
    id_: int
    type_: str
