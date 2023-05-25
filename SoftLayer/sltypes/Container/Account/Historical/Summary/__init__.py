from datetime import datetime
from SoftLayer.sltypes.Container.Account.Historical.Summary.Detail import Container_Account_Historical_Summary_Detail
from SoftLayer.sltypes.Entity import Entity

class Container_Account_Historical_Summary(Entity):
    """Historical Summary Container for account resource details"""
    details: list[Container_Account_Historical_Summary_Detail]
    endDate: datetime
    startDate: datetime
