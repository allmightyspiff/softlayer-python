# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_FlexibleCredit_Program(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_FlexibleCredit_Program'
        self.client = client

    def getAffiliatesAvailableForSelfEnrollmentByVerificationType(
        self,
        verificationTypeKeyName: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_FlexibleCredit_Affiliate]':

        data = self.client.call(
            self.service,
            'getAffiliatesAvailableForSelfEnrollmentByVerificationType',
            verificationTypeKeyName,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.FlexibleCredit.Affiliate import Affiliate
        return Affiliate(data)


    def getCompanyTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_FlexibleCredit_Company_Type]':

        data = self.client.call(
            self.service,
            'getCompanyTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.FlexibleCredit.Company.Type import Type
        return Type(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_FlexibleCredit_Program':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.FlexibleCredit.Program import Program
        return Program(data)


    def selfEnrollNewAccount(
        self,
        accountTemplate: 'SoftLayer_Account',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'selfEnrollNewAccount',
            accountTemplate,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


