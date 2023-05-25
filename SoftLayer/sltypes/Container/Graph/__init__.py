from SoftLayer.sltypes.Container.Graph.Plot import Container_Graph_Plot
from SoftLayer.sltypes.Container.Graph.Option import Container_Graph_Option
from SoftLayer.sltypes.Container.Metric.Data.Type import Container_Metric_Data_Type
from SoftLayer.sltypes.Entity import Entity

class Container_Graph(Entity):
    baseUnit: str
    endDatetime: str
    height: int
    image: str
    interval: int
    metrics: list[Container_Metric_Data_Type]
    normalizeFlag: str
    options: list[Container_Graph_Option]
    plots: list[Container_Graph_Plot]
    returnImage: bool
    startDatetime: str
    template: str
    title: str
    width: int
