from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Compliance_Report_Type(Entity):
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Compliance_Report_Type'

    def getAllObjects(self) -> list['Compliance_Report_Type']:
        data = self.client.call('SoftLayer_Compliance_Report_Type', 'getAllObjects')
        from SoftLayer.sltypes.Compliance_Report_Type import Compliance_Report_Type
        return data

    def getObject(self, identifier: int) -> 'Compliance_Report_Type':
        """Retrieve a SoftLayer_Compliance_Report_Type record."""
        data = self.client.call('SoftLayer_Compliance_Report_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Compliance_Report_Type import Compliance_Report_Type
        return data
