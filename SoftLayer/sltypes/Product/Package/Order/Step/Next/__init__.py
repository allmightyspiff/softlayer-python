from SoftLayer.sltypes.Entity import Entity

class Product_Package_Order_Step_Next(Entity):
    """This datatype simply describes which steps are next in line for ordering."""
    id_: int
    nextOrderStepId: int
    orderStepId: int
