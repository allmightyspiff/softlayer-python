from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Domain_Registration_Status(Entity):
    """SoftLayer_Dns_Domain_Registration_Status models the state of domain name. Here are the following status
codes:    *'''Active''': This domain name is active. *'''Pending Owner Approval''': Pending owner approval
for completion of transfer. *'''Pending Admin Review''': Pending admin review for transfer. *'''Pending
Registry''': Pending registry for transfer. *'''Expired''': Domain name has expired."""
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_Registration_Status'

    def getAllObjects(self) -> list['Dns_Domain_Registration_Status']:
        data = self.client.call('SoftLayer_Dns_Domain_Registration_Status', 'getAllObjects')
        from SoftLayer.sltypes.Dns_Domain_Registration_Status import Dns_Domain_Registration_Status
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_Registration_Status':
        """Retrieve a SoftLayer_Dns_Domain_Registration_Status record."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration_Status import Dns_Domain_Registration_Status
        return data
