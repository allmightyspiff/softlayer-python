from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_PSID_Xref(Entity):
    """The SoftLayer_Hardware_Component_PSID_Xref data type holds physical security ID information for hard drives"""
    componentId: int
    psid: str
