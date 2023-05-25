from SoftLayer.sltypes.Container.Product.Promotion.RequirementGroup import Container_Product_Promotion_RequirementGroup
from SoftLayer.sltypes.Location import Location
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Promotion(Entity):
    """The SoftLayer_Container_Product_Promotion data type contains information about a promotion and its
requirements."""
    code: str
    expirationDate: datetime
    locations: list[Location]
    requirementGroups: list[Container_Product_Promotion_RequirementGroup]
