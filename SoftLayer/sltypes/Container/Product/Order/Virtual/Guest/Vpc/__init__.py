from SoftLayer.sltypes.Container.Product.Order.Vpc.Subnet import Container_Product_Order_Vpc_Subnet
from SoftLayer.sltypes.Container.Product.Order.Virtual.Guest.Vpc.StorageVolume import Container_Product_Order_Virtual_Guest_Vpc_StorageVolume
from SoftLayer.sltypes.Container.Product.Order.Vpc.IpAllocation import Container_Product_Order_Vpc_IpAllocation
from SoftLayer.sltypes.Container.Product.Order.Virtual.Guest.Vpc.NetworkInterface import Container_Product_Order_Virtual_Guest_Vpc_NetworkInterface
from SoftLayer.sltypes.Container.Product.Order.Virtual.Guest import Container_Product_Order_Virtual_Guest
from SoftLayer.sltypes.Container_Product_Order_Virtual_Guest import Container_Product_Order_Virtual_Guest

class Container_Product_Order_Virtual_Guest_Vpc(Container_Product_Order_Virtual_Guest):
    additionalNetworkInterfaces: list[Container_Product_Order_Virtual_Guest_Vpc_NetworkInterface]
    crn: str
    instanceProfile: str
    ipAllocations: list[Container_Product_Order_Vpc_IpAllocation]
    overlayNetworkFlag: bool
    resourceGroup: str
    serverId: str
    servicePortCidr: str
    servicePortDns: list[str]
    servicePortGateway: str
    servicePortInterfaceId: str
    servicePortIpAddress: str
    servicePortIpAllocationId: str
    servicePortVpcId: str
    storageVolumes: list[Container_Product_Order_Virtual_Guest_Vpc_StorageVolume]
    subnets: list[Container_Product_Order_Vpc_Subnet]
    zone: str
