from SoftLayer.sltypes.Notification.Occurrence.Resource import Notification_Occurrence_Resource
from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource

class Notification_Occurrence_Resource_Network_Storage_Lockbox(Notification_Occurrence_Resource):
    """This type contains general information related to a [[SoftLayer_Network_Storage_Lockbox]] resource that is
impacted by a [[SoftLayer_Notification_Occurrence_Event]]."""
    hostname: str
    privateIp: str
    resourceType: str
