from SoftLayer.sltypes.Container.RemoteManagement.Graphs.SensorTemperature import Container_RemoteManagement_Graphs_SensorTemperature
from SoftLayer.sltypes.Container.RemoteManagement.Graphs.SensorSpeed import Container_RemoteManagement_Graphs_SensorSpeed
from SoftLayer.sltypes.Container.RemoteManagement.SensorReading import Container_RemoteManagement_SensorReading
from SoftLayer.sltypes.Entity import Entity

class Container_RemoteManagement_SensorReadingsWithGraphs(Entity):
    """The SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs contains the raw data retrieved from a
server's remote management card.  Along with the raw data, two sets of graphs will be returned.  One set of
graphs is used to display, using thermometer graphs, the temperatures (cpu(s) and system) retrieved from the
management card.  The other set is used to display speed for each of the server's fans."""
    rawData: list[Container_RemoteManagement_SensorReading]
    speedGraphs: list[Container_RemoteManagement_Graphs_SensorSpeed]
    temperatureGraphs: list[Container_RemoteManagement_Graphs_SensorTemperature]
