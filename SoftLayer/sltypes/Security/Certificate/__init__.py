from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Security_Certificate(Entity):
    certificate: str
    certificateSigningRequest: str
    commonName: str
    createDate: datetime
    id_: int
    intermediateCertificate: str
    keySize: int
    modifyDate: datetime
    notes: str
    organizationName: str
    privateKey: str
    validityBegin: datetime
    validityDays: int
    validityEnd: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Security_Certificate'

    def createObject(self, templateObject: 'Security_Certificate') -> 'Security_Certificate':
        data = self.client.call('SoftLayer_Security_Certificate', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Security_Certificate', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Security_Certificate') -> bool:
        data = self.client.call('SoftLayer_Security_Certificate', 'editObject', templateObject, id=identifier)
        return data

    def findByCommonName(self, commonName: str) -> list['Security_Certificate']:
        data = self.client.call('SoftLayer_Security_Certificate', 'findByCommonName', commonName)
        return data

    def getObject(self, identifier: int) -> 'Security_Certificate':
        """Retrieve a SoftLayer_Security_Certificate record."""
        data = self.client.call('SoftLayer_Security_Certificate', 'getObject', id=identifier)
        return data

    def getPemFormat(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Security_Certificate', 'getPemFormat', id=identifier)
        return data

    def getAssociatedServiceCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Security_Certificate', 'getAssociatedServiceCount', id=identifier)
        return data

    def getLbaasListeners(self, identifier: int) -> list['Network_LBaaS_Listener']:
        """"""
        data = self.client.call('SoftLayer_Security_Certificate', 'getLbaasListeners', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_Listener import Network_LBaaS_Listener
        return data

    def getLoadBalancerVirtualIpAddresses(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']:
        """"""
        data = self.client.call('SoftLayer_Security_Certificate', 'getLoadBalancerVirtualIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
        return data
