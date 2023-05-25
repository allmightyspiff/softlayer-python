from SoftLayer.sltypes.Ticket import Ticket
from SoftLayer.sltypes.Account import Account
from SoftLayer.sltypes.Entity import Entity

class Container_Account_Update_Response(Entity):
    """Contains data related to an account after editing its information."""
    acceptedFlag: bool
    account: Account
    ticket: Ticket
