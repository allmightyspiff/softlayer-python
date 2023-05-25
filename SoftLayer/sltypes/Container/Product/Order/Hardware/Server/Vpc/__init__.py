from SoftLayer.sltypes.Container.Product.Order.Vpc.Subnet import Container_Product_Order_Vpc_Subnet
from SoftLayer.sltypes.Container.Product.Order.Vpc.IpAllocation import Container_Product_Order_Vpc_IpAllocation
from SoftLayer.sltypes.Container.Product.Order.Hardware.Server import Container_Product_Order_Hardware_Server
from SoftLayer.sltypes.Container_Product_Order_Hardware_Server import Container_Product_Order_Hardware_Server

class Container_Product_Order_Hardware_Server_Vpc(Container_Product_Order_Hardware_Server):
    crn: str
    instanceProfile: str
    ipAllocations: list[Container_Product_Order_Vpc_IpAllocation]
    resourceGroup: str
    serverId: str
    servicePortInterfaceId: str
    servicePortIpAllocationId: str
    servicePortVpcId: str
    subnets: list[Container_Product_Order_Vpc_Subnet]
    zone: str
