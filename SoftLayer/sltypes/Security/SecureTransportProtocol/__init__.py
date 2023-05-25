from SoftLayer.sltypes.Security.SecureTransportCipher import Security_SecureTransportCipher
from SoftLayer.sltypes.Entity import Entity

class Security_SecureTransportProtocol(Entity):
    """Protocol intended for use in secure communications"""
    keyName: str
    supportedSecureTransportCiphers: list[Security_SecureTransportCipher]
