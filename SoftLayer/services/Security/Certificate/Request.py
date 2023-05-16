# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Security_Certificate_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Security_Certificate_Request'
        self.client = client

    def cancelSslOrder(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'cancelSslOrder',
            
        )
        
        return data


    def getAdministratorEmailDomains(
        self,
        commonName: str
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAdministratorEmailDomains',
            commonName
        )
        
        return data


    def getAdministratorEmailPrefixes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAdministratorEmailPrefixes',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate.Request import Request
        return Request(data)


    def getPreviousOrderData(
        self,
        
    ) -> 'SoftLayer_Container_Product_Order_Security_Certificate':

        data = self.client.call(
            self.service,
            'getPreviousOrderData',
            
        )
        from SoftLayer.datatypes.Container.Product.Order.Security.Certificate import Certificate
        return Certificate(data)


    def getSslCertificateRequests(
        self,
        accountId: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Security_Certificate_Request]':

        data = self.client.call(
            self.service,
            'getSslCertificateRequests',
            accountId,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate.Request import Request
        return Request(data)


    def resendEmail(
        self,
        emailType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'resendEmail',
            emailType
        )
        
        return data


    def validateCsr(
        self,
        csr: str,
        validityMonths: int,
        itemId: int,
        serverType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateCsr',
            csr,
            validityMonths,
            itemId,
            serverType
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


    def getOrder(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':

        data = self.client.call(
            self.service,
            'getOrder',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


    def getOrderItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Item':

        data = self.client.call(
            self.service,
            'getOrderItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return Item(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate_Request_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate.Request.Status import Status
        return Status(data)


