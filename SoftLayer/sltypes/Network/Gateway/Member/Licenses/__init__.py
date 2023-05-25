from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Gateway_Member_Licenses(Entity):
    expirationDate: datetime
    licenseKey: str
