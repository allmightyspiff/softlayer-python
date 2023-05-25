from SoftLayer.sltypes.Entity import Entity

class Product_Package_Order_Step(Entity):
    """Each package has at least 1 step to the ordering process. For server orders, there are many. Each step has
certain item categories which are displayed. This type describes the steps for each package."""
    id_: int
    step: str
