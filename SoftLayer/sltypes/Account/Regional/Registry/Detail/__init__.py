from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Regional_Registry_Detail(Entity):
    accountId: int
    createDate: datetime
    detailTypeId: int
    id_: int
    modifyDate: datetime
    regionalInternetRegistryHandleId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Regional_Registry_Detail'

    def createObject(self, templateObject: 'Account_Regional_Registry_Detail') -> 'Account_Regional_Registry_Detail':
        """Create a new detail object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'createObject', templateObject)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete an existing detail object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Regional_Registry_Detail') -> bool:
        """Edit an existing detail object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Regional_Registry_Detail':
        """Retrieve a SoftLayer_Account_Regional_Registry_Detail record."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def updateReferencedRegistrations(self, identifier: int) -> 'Container_Network_Subnet_Registration_TransactionDetails':
        """Create a transaction to update the registrations that reference this detail object."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'updateReferencedRegistrations', id=identifier)
        from SoftLayer.sltypes.Container_Network_Subnet_Registration_TransactionDetails import Container_Network_Subnet_Registration_TransactionDetails
        return data

    def validatePersonForAllRegistrars(self, identifier: int) -> list['Container_Message']:
        """Validate an existing person detail object."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'validatePersonForAllRegistrars', id=identifier)
        from SoftLayer.sltypes.Container_Message import Container_Message
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDetailType(self, identifier: int) -> 'Account_Regional_Registry_Detail_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getDetailType', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Type import Account_Regional_Registry_Detail_Type
        return data

    def getDetails(self, identifier: int) -> list['Network_Subnet_Registration_Details']:
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getDetails', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration_Details import Network_Subnet_Registration_Details
        return data

    def getProperties(self, identifier: int) -> list['Account_Regional_Registry_Detail_Property']:
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getProperties', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Property import Account_Regional_Registry_Detail_Property
        return data

    def getRegionalInternetRegistryHandle(self, identifier: int) -> 'Account_Rwhois_Handle':
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail', 'getRegionalInternetRegistryHandle', id=identifier)
        from SoftLayer.sltypes.Account_Rwhois_Handle import Account_Rwhois_Handle
        return data
