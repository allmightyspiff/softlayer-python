# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_ProofOfConcept_Approver(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_ProofOfConcept_Approver'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_ProofOfConcept_Approver]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver import Approver
        return Approver(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_ProofOfConcept_Approver':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver import Approver
        return Approver(data)


    def getRole(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_ProofOfConcept_Approver_Role':

        data = self.client.call(
            self.service,
            'getRole',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver.Role import Role
        return Role(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_ProofOfConcept_Approver_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.ProofOfConcept.Approver.Type import Type
        return Type(data)


