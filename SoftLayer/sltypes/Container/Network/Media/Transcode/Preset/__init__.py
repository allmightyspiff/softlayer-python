from SoftLayer.sltypes.Entity import Entity

class Container_Network_Media_Transcode_Preset(Entity):
    """Transcode preset is a set of configuration parameters that defines a Transcode output format.
SoftLayer_Container_Network_Media_Transcode_Preset contains a preset information defined on a Transcode
server"""
    GUID: str
    category: str
    description: str
    name: str
