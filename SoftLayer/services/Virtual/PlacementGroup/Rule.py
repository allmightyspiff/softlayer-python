# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_PlacementGroup_Rule(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_PlacementGroup_Rule'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Virtual_PlacementGroup_Rule]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.PlacementGroup.Rule import Rule
        return Rule(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_PlacementGroup_Rule':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.PlacementGroup.Rule import Rule
        return Rule(data)


