from SoftLayer.sltypes.Entity import Entity

class Container_Network_Media_Information(Entity):
    """This container class holds information on a media file such as file name, codec, frame rate and so on"""
    audioBitRate: int
    audioChannelMode: str
    audioChannels: int
    audioCodec: str
    audioSampleRate: int
    duration: float
    errorMessage: str
    file: str
    fileFormat: str
    fileSize: int
    frameRate: float
    sizeX: int
    sizeY: int
    totalFrames: int
    videoAspectX: float
    videoAspectY: int
    videoCodec: str
