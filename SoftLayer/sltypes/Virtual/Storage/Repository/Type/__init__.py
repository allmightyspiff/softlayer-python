from SoftLayer.sltypes.Entity import Entity

class Virtual_Storage_Repository_Type(Entity):
    """SoftLayer employs many different types of repositories that computing instances use as their storage volume.
SoftLayer_Virtual_Storage_Repository_Type models a single storage type. Common types of storage repositories
include networked file systems, logical volume management, and local disk volumes for swap and page file
management."""
    description: str
    name: str
