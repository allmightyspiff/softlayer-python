from SoftLayer.sltypes.Entity import Entity

class Hardware_Status(Entity):
    """SoftLayer_Hardware_Status models the inventory state of any piece of hardware in SoftLayer's inventory. Most
of these statuses are used by SoftLayer while a server is not provisioned or undergoing provisioning.
SoftLayer uses the following status codes:    *'''ACTIVE''': This server is active and in use. *'''DEPLOY''':
Used during server provisioning. *'''DEPLOY2''': Used during server provisioning. *'''MACWAIT''': Used during
server provisioning. *'''RECLAIM''': This server has been reclaimed by SoftLayer and is awaiting de-
provisioning.   Servers in production and in use should stay in the ACTIVE state. If a server's status ever
reads anything else then please contact SoftLayer support."""
    id_: int
    status: str
