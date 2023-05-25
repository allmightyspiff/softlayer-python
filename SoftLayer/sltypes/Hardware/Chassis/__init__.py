from SoftLayer.sltypes.Entity import Entity

class Hardware_Chassis(Entity):
    """Every piece of hardware in SoftLayer's datacenters, including customer servers, are housed in one of many
hardware chassis. The SoftLayer_Hardware_Chassis data type defines these chassis."""
    formFactorId: int
    id_: int
    manufacturer: str
    name: str
    unitSize: int
    version: str
