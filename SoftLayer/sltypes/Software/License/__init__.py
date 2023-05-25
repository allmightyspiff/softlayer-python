from SoftLayer.sltypes.Entity import Entity

class Software_License(Entity):
    """This class describes a specific type of license, like a Microsoft Windows Site License, a GPL license, or a
license of another type."""
    id_: int
    softwareDescriptionId: int
