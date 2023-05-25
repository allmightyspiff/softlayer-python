from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Metric.Tracking.Object.Data import Metric_Tracking_Object_Data
from SoftLayer.sltypes.Virtual.Guest import Virtual_Guest
from SoftLayer.sltypes.Container.Account.Historical.Summary.Detail import Container_Account_Historical_Summary_Detail
from SoftLayer.sltypes.Container_Account_Historical_Summary_Detail import Container_Account_Historical_Summary_Detail

class Container_Account_Historical_Summary_Detail_Uptime(Container_Account_Historical_Summary_Detail):
    """Historical Summary Details Container for a host resource uptime"""
    cloudComputingInstance: Virtual_Guest
    data: list[Metric_Tracking_Object_Data]
    hardware: Hardware
