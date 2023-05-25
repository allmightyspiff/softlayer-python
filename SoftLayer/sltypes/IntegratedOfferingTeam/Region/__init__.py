from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class IntegratedOfferingTeam_Region(Entity):
    """This class represents an Integrated Offering Team region."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'IntegratedOfferingTeam_Region'

    def getAllObjects(self) -> list['IntegratedOfferingTeam_Container_Region']:
        data = self.client.call('IntegratedOfferingTeam_Region', 'getAllObjects')
        return data

    def getRegionLeads(self) -> list['IntegratedOfferingTeam_Container_Region_Lead']:
        data = self.client.call('IntegratedOfferingTeam_Region', 'getRegionLeads')
        return data
