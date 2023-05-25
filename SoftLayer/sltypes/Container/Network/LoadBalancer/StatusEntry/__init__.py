from SoftLayer.sltypes.Entity import Entity

class Container_Network_LoadBalancer_StatusEntry(Entity):
    """The LoadBalancer_StatusEntry object stores information about the current status of a particular load balancer
service.   It is a data container that cannot be edited, deleted, or saved.   It is returned exclusively by
the getStatus method on the [[SoftLayer_Network_LoadBalancer_Service]] service"""
    content: str
    label: str
