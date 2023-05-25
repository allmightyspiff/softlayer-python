from SoftLayer.sltypes.Entity import Entity

class Network_Gateway_Member_Passwords(Entity):
    id_: int
    memberId: int
    password: str
    username: str
