# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_ProofOfConcept_Approver_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_ProofOfConcept_Approver_Type'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_ProofOfConcept_Approver_Type':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver.Type import Type
        return Type(data)


    def getApprovers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_ProofOfConcept_Approver]':

        data = self.client.call(
            self.service,
            'getApprovers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver import Approver
        return Approver(data)


