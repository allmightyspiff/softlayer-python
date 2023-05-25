from SoftLayer.sltypes.Entity import Entity

class User_Employee_Department(Entity):
    """SoftLayer_User_Employee_Department models a department within SoftLayer's internal employee hierarchy. Common
departments include Support, Sales, Accounting, Development, Systems, and Networking."""
    name: str
