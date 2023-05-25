from SoftLayer.sltypes.Container.Metric.Data.Type import Container_Metric_Data_Type
from SoftLayer.sltypes.Container.Graph.Plot.Coordinate import Container_Graph_Plot_Coordinate
from SoftLayer.sltypes.Entity import Entity

class Container_Graph_Plot(Entity):
    data: list[Container_Graph_Plot_Coordinate]
    metric: Container_Metric_Data_Type
    unit: str
