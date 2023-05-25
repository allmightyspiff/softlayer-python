from SoftLayer.sltypes.Entity import Entity

class Notification_Preference(Entity):
    """Retrieve details for preferences.  Preferences are used to allow the subscriber to modify their subscription
in various ways.  Details such as friendly name, keyname maximum and minimum values can be retrieved.  These
provide details to help configure subscriber preferences correctly."""
    description: str
    id_: int
    keyName: str
    maximumValue: str
    minimumValue: str
    name: str
    units: str
    value: str
