from SoftLayer.sltypes.Software.Component import Software_Component
from SoftLayer.sltypes.Software_Component import Software_Component
from SoftLayer import BaseClient

class Software_Component_AntivirusSpyware(Software_Component):
    """This object specifies a specific type of Software Component:  An Anti-virus/spyware instance. Anti-
virus/spyware installations have specific properties and methods such as
SoftLayer_Software_Component_AntivirusSpyware::updateAntivirusSpywarePolicy. Defaults are initiated by this
object."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_Component_AntivirusSpyware'

    def getObject(self, identifier: int) -> 'Software_Component_AntivirusSpyware':
        """Retrieve a SoftLayer_Software_Component_AntivirusSpyware record."""
        data = self.client.call('SoftLayer_Software_Component_AntivirusSpyware', 'getObject', id=identifier)
        from SoftLayer.sltypes.Software_Component_AntivirusSpyware import Software_Component_AntivirusSpyware
        return data

    def updateAntivirusSpywarePolicy(self, identifier: int, newPolicy: str, enforce: bool) -> bool:
        """Update an anti-virus/spyware policy."""
        data = self.client.call('SoftLayer_Software_Component_AntivirusSpyware', 'updateAntivirusSpywarePolicy', newPolicy, enforce, id=identifier)
        return data
