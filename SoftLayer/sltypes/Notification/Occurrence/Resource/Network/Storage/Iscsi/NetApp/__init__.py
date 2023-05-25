from SoftLayer.sltypes.Notification.Occurrence.Resource import Notification_Occurrence_Resource
from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource

class Notification_Occurrence_Resource_Network_Storage_Iscsi_NetApp(Notification_Occurrence_Resource):
    """This type contains general information related to a [[SoftLayer_Network_Storage_Iscsi_NetApp]] resource that
is impacted by a [[SoftLayer_Notification_Occurrence_Event]]."""
    hostname: str
    privateIp: str
    resourceType: str
