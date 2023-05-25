from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Domain_Registration_Registrant_Verification_Status(Entity):
    """SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status models the state of the registrant. Here are
the following status codes:    *'''Admin Reviewing''': The registrant data has been submitted and being
reviewed by compliance team. *'''Pending''': The verification process has been inititated, and verification
email will be sent. *'''Suspended''': The registrant has failed verification and the domain has been
suspended. *'''Verified''': The registrant has been validated. *'''Verifying''': The verification process has
been initiated and is waiting for registrant response. *'''Unverified''': The verification process has not
been inititated."""
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status'

    def getAllObjects(self) -> list['Dns_Domain_Registration_Registrant_Verification_Status']:
        data = self.client.call('SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status', 'getAllObjects')
        from SoftLayer.sltypes.Dns_Domain_Registration_Registrant_Verification_Status import Dns_Domain_Registration_Registrant_Verification_Status
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_Registration_Registrant_Verification_Status':
        """Retrieve a SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status record."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration_Registrant_Verification_Status import Dns_Domain_Registration_Registrant_Verification_Status
        return data
