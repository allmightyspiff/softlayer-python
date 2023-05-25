from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader(Entity):
    """The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader data type contains
information for specific responses from the modify response header API."""
    delimiter: str
    description: str
    headers: list[str]
    modResHeaderUniqueId: str
    path: str
    type_: str
    uniqueId: str
