# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Affiliation(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Affiliation'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Account_Affiliation',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Affiliation':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Affiliation import Affiliation
        return Affiliation(data)


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Account_Affiliation',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getAccountAffiliationsByAffiliateId(
        self,
        affiliateId: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Affiliation]':

        data = self.client.call(
            self.service,
            'getAccountAffiliationsByAffiliateId',
            affiliateId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Affiliation import Affiliation
        return Affiliation(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Affiliation':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Affiliation import Affiliation
        return Affiliation(data)


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


