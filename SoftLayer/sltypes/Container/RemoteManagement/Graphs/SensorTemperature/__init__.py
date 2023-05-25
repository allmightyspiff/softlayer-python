from SoftLayer.sltypes.Entity import Entity

class Container_RemoteManagement_Graphs_SensorTemperature(Entity):
    """The SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature contains graphs to display the cpu(s) and
system temperatures retrieved from the management card using thermometer graphs."""
    graph: str
    title: str
