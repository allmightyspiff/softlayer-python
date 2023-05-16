# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class IntegratedOfferingTeam_Region(object):

    def __init__(self, client: Client) -> None:
        self.service = 'IntegratedOfferingTeam_Region'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[IntegratedOfferingTeam_Container_Region]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        
        return data


    def getRegionLeads(
        self,
        
    ) -> 'list[IntegratedOfferingTeam_Container_Region_Lead]':

        data = self.client.call(
            self.service,
            'getRegionLeads',
            
        )
        
        return data


