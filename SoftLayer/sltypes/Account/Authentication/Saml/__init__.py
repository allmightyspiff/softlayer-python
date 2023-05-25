from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Authentication_Saml(Entity):
    accountId: str
    certificate: str
    certificateFingerprint: str
    entityId: str
    id_: int
    serviceProviderCertificate: str
    serviceProviderEntityId: str
    serviceProviderPublicKey: str
    serviceProviderSingleLogoutEncoding: str
    serviceProviderSingleLogoutUrl: str
    serviceProviderSingleSignOnEncoding: str
    serviceProviderSingleSignOnUrl: str
    singleLogoutEncoding: str
    singleLogoutUrl: str
    singleSignOnEncoding: str
    singleSignOnUrl: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Authentication_Saml'

    def createObject(self, templateObject: 'Account_Authentication_Saml') -> 'Account_Authentication_Saml':
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'createObject', templateObject)
        from SoftLayer.sltypes.Account_Authentication_Saml import Account_Authentication_Saml
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Authentication_Saml') -> bool:
        """Edit the object by passing in a modified instance of the object."""
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'editObject', templateObject, id=identifier)
        return data

    def getMetadata(self, identifier: int) -> str:
        """Get the service provider meta data."""
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'getMetadata', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Authentication_Saml':
        """Retrieve a SoftLayer_Account_Authentication_Saml record."""
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Saml import Account_Authentication_Saml
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAttributes(self, identifier: int) -> list['Account_Authentication_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Account_Authentication_Saml', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Attribute import Account_Authentication_Attribute
        return data
