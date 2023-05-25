from SoftLayer.sltypes.Container.User.Customer.Profile.Event.HyperWarp.ProfileChange.EventProperties import Container_User_Customer_Profile_Event_HyperWarp_ProfileChange_EventProperties
from SoftLayer.sltypes.Container.User.Customer.Profile.Event.HyperWarp.ProfileChange.Context import Container_User_Customer_Profile_Event_HyperWarp_ProfileChange_Context
from SoftLayer.sltypes.Entity import Entity

class Container_User_Customer_Profile_Event_HyperWarp_ProfileChange(Entity):
    account_id: str
    context: Container_User_Customer_Profile_Event_HyperWarp_ProfileChange_Context
    event_id: str
    event_properties: Container_User_Customer_Profile_Event_HyperWarp_ProfileChange_EventProperties
    event_type: str
    publisher: str
    timestamp: str
    version: str
