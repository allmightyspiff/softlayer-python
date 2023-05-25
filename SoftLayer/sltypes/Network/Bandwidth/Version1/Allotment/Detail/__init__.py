from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Bandwidth_Version1_Allotment_Detail(Entity):
    """The SoftLayer_Network_Bandwidth_Version1_Allotment_Detail data type contains specific information relating to
a single bandwidth allotment record."""
    allocationId: int
    bandwidthAllotmentId: int
    effectiveDate: datetime
    endEffectiveDate: datetime
    id_: int
    serviceProviderId: int
