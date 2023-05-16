# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Firewall_Update_Request_Rule(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Firewall_Update_Request_Rule'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Firewall_Update_Request_Rule,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Firewall_Update_Request_Rule':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request.Rule import Rule
        return Rule(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Firewall_Update_Request_Rule':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request.Rule import Rule
        return Rule(data)


    def validateRule(
        self,
        rule: SoftLayer_Network_Firewall_Update_Request_Rule,
        applyToComponentId: int,
        applyToAclId: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'validateRule',
            rule,
            applyToComponentId,
            applyToAclId
        )
        
        return data


    def getFirewallUpdateRequest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Firewall_Update_Request':

        data = self.client.call(
            self.service,
            'getFirewallUpdateRequest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request import Request
        return Request(data)


