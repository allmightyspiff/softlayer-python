from SoftLayer.sltypes.Entity import Entity

class Auxiliary_Notification_Emergency_Signature(Entity):
    """Every SoftLayer_Auxiliary_Notification_Emergency has a signatureId that references a
SoftLayer_Auxiliary_Notification_Emergency_Signature data type.  The signature is the user or group
responsible for the current event."""
    name: str
