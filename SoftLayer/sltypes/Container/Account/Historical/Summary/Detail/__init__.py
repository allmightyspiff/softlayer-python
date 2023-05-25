from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Account_Historical_Summary_Detail(Entity):
    """Historical Summary Details Container for a resource's data"""
    endDate: datetime
    startDate: datetime
