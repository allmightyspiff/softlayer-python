from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Property(Entity):
    """This is used for storing various items about the order. Currently used for storing additional raid
information when ordering servers. This is optional"""
    name: str
    value: str
