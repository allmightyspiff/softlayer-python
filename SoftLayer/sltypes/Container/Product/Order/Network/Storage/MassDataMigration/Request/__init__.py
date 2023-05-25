from SoftLayer.sltypes.Container.Network.Storage.MassDataMigration.Request.Address import Container_Network_Storage_MassDataMigration_Request_Address
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Storage_MassDataMigration_Request(Container_Product_Order):
    """This datatype is to be used for mass data migration requests."""
    address1: str
    address2: str
    addressAttention: str
    addressNickname: str
    city: str
    companyName: str
    cosAccountId: str
    cosBucketName: str
    country: str
    eth1DefaultGateway: str
    eth1Netmask: str
    eth1StaticIp: str
    eth3Netmask: str
    eth3StaticIp: str
    keyContactEmails: list[str]
    keyContactNames: list[str]
    keyContactPhoneNumbers: list[str]
    keyContactRoles: list[str]
    postalCode: str
    requestName: str
    shippingAddress: Container_Network_Storage_MassDataMigration_Request_Address
    state: str
