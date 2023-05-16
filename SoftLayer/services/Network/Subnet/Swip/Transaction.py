# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet_Swip_Transaction(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet_Swip_Transaction'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def findMyTransactions(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_Swip_Transaction]':
        data = self.client.call(
            self.service,
            'findMyTransactions',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.Swip.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Swip_Transaction':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Swip.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def removeAllSubnetSwips(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'removeAllSubnetSwips',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeSwipData(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeSwipData',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def resendSwipData(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'resendSwipData',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def swipAllSubnets(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'swipAllSubnets',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def updateAllSubnetSwips(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'updateAllSubnetSwips',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getSubnet(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':
        data = self.client.call(
            self.service,
            'getSubnet',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)


