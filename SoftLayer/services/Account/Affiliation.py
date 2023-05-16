# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Affiliation(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Affiliation'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Account_Affiliation,
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
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Account_Affiliation
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
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
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Affiliation':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Affiliation import Affiliation
        return Affiliation(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


