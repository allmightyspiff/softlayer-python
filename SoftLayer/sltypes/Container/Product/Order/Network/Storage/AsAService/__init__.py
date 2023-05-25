from SoftLayer.sltypes.Network.Storage.Iscsi.OS.Type import Network_Storage_Iscsi_OS_Type
from SoftLayer.sltypes.Network.Storage.DedicatedCluster import Network_Storage_DedicatedCluster
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Storage_AsAService(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order for Storage as a Service."""
    dedicatedCluster: Network_Storage_DedicatedCluster
    duplicateOriginSnapshotId: int
    duplicateOriginVolumeId: int
    iops: int
    isDependentDuplicateFlag: bool
    originVolumeId: int
    originVolumeScheduleId: int
    osFormatType: Network_Storage_Iscsi_OS_Type
    volumeSize: int
