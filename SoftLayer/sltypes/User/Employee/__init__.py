from SoftLayer.sltypes.User.Interface import User_Interface
from SoftLayer.sltypes.User_Interface import User_Interface

class User_Employee(User_Interface):
    """A SoftLayer_User_Employee models a single SoftLayer employee for the purposes of ticket updates created by
SoftLayer employees. SoftLayer portal and API users cannot see individual employee names in ticket responses.
SoftLayer employees can be assigned to customer accounts as a personal support representative.  Employee
names and email will be available if an employee is assigned to the account."""
    displayName: str
    email: str
    employeeDepartmentId: int
    firstName: str
    lastName: str
    username: str
