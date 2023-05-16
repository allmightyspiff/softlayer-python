# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Firewall_Update_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Firewall_Update_Request'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Firewall_Update_Request,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Firewall_Update_Request':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request import Request
        return Request(data)


    def getFirewallUpdateRequestRuleAttributes(
        self,
        
    ) -> 'SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute':

        data = self.client.call(
            self.service,
            'getFirewallUpdateRequestRuleAttributes',
            
        )
        from SoftLayer.datatypes.Container.Utility.Network.Firewall.Rule.Attribute import Attribute
        return Attribute(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Firewall_Update_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request import Request
        return Request(data)


    def updateRuleNote(
        self,
        fwRule: SoftLayer_Network_Component_Firewall_Rule,
        note: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateRuleNote',
            fwRule,
            note
        )
        
        return data


    def getAuthorizingUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Interface':

        data = self.client.call(
            self.service,
            'getAuthorizingUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Interface import Interface
        return Interface(data)


    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkComponentFirewall(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component_Firewall':

        data = self.client.call(
            self.service,
            'getNetworkComponentFirewall',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return Firewall(data)


    def getRules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Firewall_Update_Request_Rule]':

        data = self.client.call(
            self.service,
            'getRules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request.Rule import Rule
        return Rule(data)


