from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Workspace_Order_LicenseKey(Entity):
    """This is the datatype that can be populated by the customer to provide license key information for VMware
orders."""
    key: str
    name: str
    type_: str
