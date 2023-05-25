from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Exception_Brand_Creation(Entity):
    """Throw this exception if there are validation errors. The types are specified in
SoftLayer_Brand_Creation_Input including: KEY_NAME, PREFIX, NAME, LONG_NAME, SUPPORT_POLICY,
POLICY_ACKNOWLEDGEMENT_FLAG, etc."""
    message: str
    type_: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Exception_Brand_Creation'
