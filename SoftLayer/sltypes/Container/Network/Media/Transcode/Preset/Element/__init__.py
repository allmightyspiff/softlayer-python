from SoftLayer.sltypes.Container.Network.Media.Transcode.Preset.Element.Option import Container_Network_Media_Transcode_Preset_Element_Option
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Media_Transcode_Preset_Element(Entity):
    """Transcode preset element"""
    additionalElements: list[Container_Network_Media_Transcode_Preset_Element_Option]
    defaultValue: str
    description: str
    enabled: bool
    extendedDescription: str
    hidden: bool
    maximumValue: int
    minimumValue: int
    name: str
    parentName: str
    type_: str
