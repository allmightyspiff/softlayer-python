from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Security_Certificate_Request(Entity):
    """The SoftLayer_Security_Certificate_Request data type is used to view details about your SSL certificate
order. This contains data that is required by a Certificate Authority to place an SSL certificate order."""
    accountId: int
    approverEmailAddress: str
    certificateSigningRequest: str
    commonName: str
    createDate: datetime
    effectiveDate: datetime
    expirationDate: datetime
    id_: int
    modifyDate: datetime
    statusId: int
    technicalContactEmailAddress: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Security_Certificate_Request'

    def cancelSslOrder(self, identifier: int) -> bool:
        """Cancels a pending SSL certificate order at the Certificate Authority"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'cancelSslOrder', id=identifier)
        return data

    def getAdministratorEmailDomains(self, commonName: str) -> list[str]:
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getAdministratorEmailDomains', commonName)
        return data

    def getAdministratorEmailPrefixes(self) -> list[str]:
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getAdministratorEmailPrefixes')
        return data

    def getObject(self, identifier: int) -> 'Security_Certificate_Request':
        """Retrieve a SoftLayer_Security_Certificate_Request record."""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getObject', id=identifier)
        from SoftLayer.sltypes.Security_Certificate_Request import Security_Certificate_Request
        return data

    def getPreviousOrderData(self, identifier: int) -> 'Container_Product_Order_Security_Certificate':
        """Returns previous SSL certificate order data."""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getPreviousOrderData', id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Security_Certificate import Container_Product_Order_Security_Certificate
        return data

    def getSslCertificateRequests(self, accountId: int) -> list['Security_Certificate_Request']:
        """Returns all the SSL certificate requests"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getSslCertificateRequests', accountId)
        from SoftLayer.sltypes.Security_Certificate_Request import Security_Certificate_Request
        return data

    def resendEmail(self, identifier: int, emailType: str) -> bool:
        """Have the Certificate Authority send various emails"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'resendEmail', emailType, id=identifier)
        return data

    def validateCsr(self, csr: str, validityMonths: int, itemId: int, serverType: str) -> bool:
        """Validates a Certificate Signing Request (CSR) with the certificate authority (CA)."""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'validateCsr', csr, validityMonths, itemId, serverType)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getOrder(self, identifier: int) -> 'Billing_Order':
        """"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getOrder', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getOrderItem(self, identifier: int) -> 'Billing_Order_Item':
        """"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getOrderItem', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getStatus(self, identifier: int) -> 'Security_Certificate_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Security_Certificate_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Security_Certificate_Request_Status import Security_Certificate_Request_Status
        return data
