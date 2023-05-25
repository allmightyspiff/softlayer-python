from SoftLayer.sltypes.Container.Network.Media.Transcode.Job.Watermark.Position import Container_Network_Media_Transcode_Job_Watermark_Position
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Media_Transcode_Job_Watermark(Entity):
    endTime: int
    fileName: str
    position: Container_Network_Media_Transcode_Job_Watermark_Position
    startTime: int
    text: str
    transparencyPercentage: int
