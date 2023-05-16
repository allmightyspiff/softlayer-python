# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Firewall_Template(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Firewall_Template'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Firewall_Template]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Firewall.Template import Template
        return Template(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Firewall_Template':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Firewall.Template import Template
        return Template(data)


    def getRules(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Firewall_Template_Rule]':

        data = self.client.call(
            self.service,
            'getRules',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Firewall.Template.Rule import Rule
        return Rule(data)


