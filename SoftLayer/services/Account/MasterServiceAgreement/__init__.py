# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_MasterServiceAgreement(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_MasterServiceAgreement'
        self.client = client

    def getFile(
        self,
        
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'getFile',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_MasterServiceAgreement':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.MasterServiceAgreement import MasterServiceAgreement
        return MasterServiceAgreement(data)


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


