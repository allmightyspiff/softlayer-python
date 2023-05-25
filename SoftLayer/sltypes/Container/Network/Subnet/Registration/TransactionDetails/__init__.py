from SoftLayer.sltypes.Container.Network.Subnet.Registration.SubnetReference import Container_Network_Subnet_Registration_SubnetReference
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Subnet_Registration_TransactionDetails(Entity):
    """SoftLayer_Container_Subnet_Registration_TransactionDetails is provided to return details of a newly created
Subnet Registration Transaction."""
    subnetReferences: list[Container_Network_Subnet_Registration_SubnetReference]
    transactionId: int
