from SoftLayer.sltypes.Notification.Occurrence.Resource import Notification_Occurrence_Resource
from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource

class Notification_Occurrence_Resource_Hardware(Notification_Occurrence_Resource):
    """This type contains general information related to a [[SoftLayer_Hardware]] resource that is impacted by a
[[SoftLayer_Notification_Occurrence_Event]]."""
    hostname: str
    privateIp: str
    publicIp: str
    resourceType: str
