from SoftLayer.sltypes.Entity import Entity

class Product_Item_Price_Account_Restriction(Entity):
    """The SoftLayer_Product_Item_Price data type gives more information about the item price restrictions.  An item
price may be restricted to one or more accounts. If the item price is restricted to an account, only that
account will see the restriction details."""
    accountId: int
    id_: int
    itemPriceId: int
