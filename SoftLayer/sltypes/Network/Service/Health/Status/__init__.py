from SoftLayer.sltypes.Entity import Entity

class Network_Service_Health_Status(Entity):
    """Many general services that SoftLayer provides are marked by a status message. These health messages give
portal users a quick way of determining the state of a SoftLayer service. Services range from backbones to
VPN endpoints and routers. Generally a health status is either "Up" or "Down"."""
    name: str
