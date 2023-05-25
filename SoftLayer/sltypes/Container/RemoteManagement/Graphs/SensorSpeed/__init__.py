from SoftLayer.sltypes.Entity import Entity

class Container_RemoteManagement_Graphs_SensorSpeed(Entity):
    """The SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed contains graphs to  display speed for each of the
server's fans.  Fan speeds are gathered from the server's remote management card."""
    graph: str
    title: str
