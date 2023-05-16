# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet_Registration(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet_Registration'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def clearRegistration(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'clearRegistration',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Network_Subnet_Registration,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Subnet_Registration':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return SL_Registration(data)

# This file was automatically generated with tools/generateTypes.py
    def createObjects(
        self,
        templateObjects: SoftLayer_Network_Subnet_Registration,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration]':
        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return SL_Registration(data)

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_Subnet_Registration
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editRegistrationAttachedDetails(
        self,
        personObjectSkeleton: SoftLayer_Network_Subnet_Registration_Details,
        networkObjectSkeleton: SoftLayer_Network_Subnet_Registration_Details
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editRegistrationAttachedDetails',
            personObjectSkeleton,
            networkObjectSkeleton
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Registration':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return SL_Registration(data)

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
    def getDetailReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration_Details]':
        data = self.client.call(
            self.service,
            'getDetailReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Details import Details
        return SL_Details(data)

# This file was automatically generated with tools/generateTypes.py
    def getEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration_Event]':
        data = self.client.call(
            self.service,
            'getEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Event import Event
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkDetail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':
        data = self.client.call(
            self.service,
            'getNetworkDetail',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return SL_Detail(data)

# This file was automatically generated with tools/generateTypes.py
    def getPersonDetail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':
        data = self.client.call(
            self.service,
            'getPersonDetail',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return SL_Detail(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegionalInternetRegistry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Regional_Internet_Registry':
        data = self.client.call(
            self.service,
            'getRegionalInternetRegistry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Regional.Internet.Registry import Registry
        return SL_Registry(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegionalInternetRegistryHandle(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Rwhois_Handle':
        data = self.client.call(
            self.service,
            'getRegionalInternetRegistryHandle',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Rwhois.Handle import Handle
        return SL_Handle(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Registration_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Status import Status
        return SL_Status(data)

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


