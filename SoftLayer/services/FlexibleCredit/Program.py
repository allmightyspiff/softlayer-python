# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_FlexibleCredit_Program(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_FlexibleCredit_Program'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAffiliatesAvailableForSelfEnrollmentByVerificationType(
        self,
        verificationTypeKeyName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_FlexibleCredit_Affiliate]':
        data = self.client.call(
            self.service,
            'getAffiliatesAvailableForSelfEnrollmentByVerificationType',
            verificationTypeKeyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.FlexibleCredit.Affiliate import Affiliate
        return SL_Affiliate(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_FlexibleCredit_Program':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.FlexibleCredit.Program import Program
        return SL_Program(data)

# This file was automatically generated with tools/generateTypes.py
    def selfEnrollNewAccount(
        self,
        accountTemplate: SoftLayer_Account,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'selfEnrollNewAccount',
            accountTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)


