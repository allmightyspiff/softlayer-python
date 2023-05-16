# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway_Precheck(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway_Precheck'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Precheck':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Precheck import Precheck
        return SL_Precheck(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrecheckStatus(
        self,
        gatewayId: int,
        getRollbackPrecheck: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Gateway_Precheck]':
        data = self.client.call(
            self.service,
            'getPrecheckStatus',
            gatewayId,
            getRollbackPrecheck,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway.Precheck import Precheck
        return SL_Precheck(data)

# This file was automatically generated with tools/generateTypes.py
    def licenseManagementPrecheck(
        self,
        gatewayId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'licenseManagementPrecheck',
            gatewayId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def osReloadPrecheck(
        self,
        gatewayId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'osReloadPrecheck',
            gatewayId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def upgradePrecheck(
        self,
        gatewayId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'upgradePrecheck',
            gatewayId
        )
        
        return data


