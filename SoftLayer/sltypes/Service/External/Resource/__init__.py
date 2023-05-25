from SoftLayer.sltypes.Entity import Entity

class Service_External_Resource(Entity):
    """The SoftLayer_Service_External_Resource is a placeholder that references a service being provided outside of
the standard SoftLayer system."""
    accountId: int
    externalIdentifier: str
    id_: int
