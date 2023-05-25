from SoftLayer.sltypes.Entity import Entity

class Location_Group_Location_CrossReference(Entity):
    id_: int
    locationGroupId: int
    locationId: int
    priority: int
