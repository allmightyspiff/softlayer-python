from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl(Entity):
    """SoftLayer_Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl provides specific details is a
container which contains the cdn urls associated with an object storage account"""
    datacenter: str
    flashUrl: str
    httpUrl: str
