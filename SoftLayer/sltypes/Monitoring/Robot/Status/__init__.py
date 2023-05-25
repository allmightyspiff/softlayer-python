from SoftLayer.sltypes.Entity import Entity

class Monitoring_Robot_Status(Entity):
    """DEPRECATED. Your monitoring robot will be in "Active" status under normal circumstances. If you perform an OS
reload, your robot will be in "Reclaim" status until it's reloaded on your server or virtual server.
Advanced monitoring system requires "Nimsoft Monitoring (Advanced)" service running and TCP ports 48000 -
48020 to be open on your server or virtual server. Monitoring agents cannot be managed nor can the usage data
be updated if these ports are closed. Your monitoring robot will be in "Limited Connectivity" status if our
monitoring management system cannot communicate with your system.   See
[[SoftLayer_Monitoring_Robot::resetStatus|resetStatus]] service for more details."""
    description: str
    id_: int
    name: str
