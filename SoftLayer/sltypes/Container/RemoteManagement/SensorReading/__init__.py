from SoftLayer.sltypes.Entity import Entity

class Container_RemoteManagement_SensorReading(Entity):
    """The SoftLayer_Container_RemoteManagement_SensorReadings contains sensor information retrieved from a server's
remote management card."""
    lowerCritical: str
    lowerNonCritical: str
    lowerNonRecoverable: str
    sensorId: str
    sensorReading: str
    sensorUnits: str
    status: str
    upperCritical: str
    upperNonCritical: str
    upperNonRecoverable: str
