from SoftLayer.sltypes.Entity import Entity

class Resource_Group_Template_Member(Entity):
    maxQuantity: int
    minQuantity: int
    roleId: int
    templateId: int
