from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_SecurityGroup(Entity):
    """The SoftLayer_Network_SecurityGroup data type contains general information for a single security group. A
security group contains a set of IP filter [[SoftLayer_Network_SecurityGroup_Rule (type)|rules]] that define
how to handle incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a
virtual server instance and a set of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding
(type)|bindings]] to associate virtual guest network components with the security group."""
    createDate: datetime
    description: str
    id_: int
    metadata: str
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_SecurityGroup'

    def addRules(self, identifier: int, ruleTemplates: 'Network_SecurityGroup_Rule') -> 'Network_SecurityGroup_RequestRules':
        """Add new rules to a security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'addRules', ruleTemplates, id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_RequestRules import Network_SecurityGroup_RequestRules
        return data

    def attachNetworkComponents(self, identifier: int, networkComponentIds: int) -> 'Network_SecurityGroup_Request':
        """Attach network components to a security group by creating a network component binding."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'attachNetworkComponents', networkComponentIds, id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_Request import Network_SecurityGroup_Request
        return data

    def createObject(self, templateObject: 'Network_SecurityGroup') -> 'Network_SecurityGroup':
        """Create a new security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Network_SecurityGroup') -> list['Network_SecurityGroup']:
        """Create new security groups."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Network_SecurityGroup') -> bool:
        """Delete security groups."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'deleteObjects', templateObjects)
        return data

    def detachNetworkComponents(self, identifier: int, networkComponentIds: int) -> 'Network_SecurityGroup_Request':
        """Detach network components from a security group by deleting its network component binding."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'detachNetworkComponents', networkComponentIds, id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_Request import Network_SecurityGroup_Request
        return data

    def editObject(self, identifier: int, templateObject: 'Network_SecurityGroup') -> bool:
        """Edit a security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Network_SecurityGroup') -> bool:
        """Edit security groups."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'editObjects', templateObjects)
        return data

    def editRules(self, identifier: int, ruleTemplates: 'Network_SecurityGroup_Rule') -> 'Network_SecurityGroup_RequestRules':
        """Edit rules that belong to a security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'editRules', ruleTemplates, id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_RequestRules import Network_SecurityGroup_RequestRules
        return data

    def getAllObjects(self) -> list['Network_SecurityGroup']:
        """Get all security groups."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getAllObjects')
        return data

    def getLimits(self) -> list['Container_Network_SecurityGroup_Limit']:
        """List the current security group limits"""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getLimits')
        from SoftLayer.sltypes.Container_Network_SecurityGroup_Limit import Container_Network_SecurityGroup_Limit
        return data

    def getObject(self, identifier: int) -> 'Network_SecurityGroup':
        """Retrieve a SoftLayer_Network_SecurityGroup record."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getObject', id=identifier)
        return data

    def getSupportedDataCenters(self) -> list['Location']:
        """List the data centers that currently support the use of security groups."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getSupportedDataCenters')
        from SoftLayer.sltypes.Location import Location
        return data

    def removeRules(self, identifier: int, ruleIds: int) -> 'Network_SecurityGroup_RequestRules':
        """Remove rules from a security group."""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'removeRules', ruleIds, id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_RequestRules import Network_SecurityGroup_RequestRules
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getNetworkComponentBindings(self, identifier: int) -> list['Virtual_Network_SecurityGroup_NetworkComponentBinding']:
        """"""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getNetworkComponentBindings', id=identifier)
        from SoftLayer.sltypes.Virtual_Network_SecurityGroup_NetworkComponentBinding import Virtual_Network_SecurityGroup_NetworkComponentBinding
        return data

    def getOrderBindings(self, identifier: int) -> list['Network_SecurityGroup_OrderBinding']:
        """"""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getOrderBindings', id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_OrderBinding import Network_SecurityGroup_OrderBinding
        return data

    def getRules(self, identifier: int) -> list['Network_SecurityGroup_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_SecurityGroup', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup_Rule import Network_SecurityGroup_Rule
        return data
