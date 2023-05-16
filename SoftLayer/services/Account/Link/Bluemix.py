# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Link_Bluemix(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Link_Bluemix'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Link_Bluemix':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Link.Bluemix import Bluemix
        return Bluemix(data)


    def getSupportTierType(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportTierType',
            
        )
        
        return data


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


    def getServiceProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':

        data = self.client.call(
            self.service,
            'getServiceProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return Provider(data)


