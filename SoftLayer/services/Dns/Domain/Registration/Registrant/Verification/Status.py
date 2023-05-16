# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Registrant.Verification.Status import Status
        return Status(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Registrant.Verification.Status import Status
        return Status(data)


