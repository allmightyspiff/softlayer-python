from SoftLayer.sltypes.Entity import Entity

class Network_Storage_MassDataMigration_Request_DeviceConfiguration(Entity):
    """The SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration data type contains settings such
networking, COS account, which needs to be configured on device for a Mass Data Migration Request."""
    cosAccountId: int
    cosBucket: str
    eth1Gateway: str
    eth1IpAddress: str
    eth1Netmask: str
    eth3Gateway: str
    eth3IpAddress: str
    eth3Netmask: str
    id_: int
    password: str
    poolLockPassword: str
    requestId: int
    s3Url: str
    shareName: str
    username: str
