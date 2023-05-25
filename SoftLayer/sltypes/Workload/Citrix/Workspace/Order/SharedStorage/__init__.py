from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Workspace_Order_SharedStorage(Entity):
    """This is the datatype that can be populated by the customer to provide NFS shared storage information for
VMware orders."""
    iops: str
    quantity: int
    size: str
    volume: int
