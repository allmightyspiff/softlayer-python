# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Package_Server_Option(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Package_Server_Option'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllOptions(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package_Server_Option]':
        data = self.client.call(
            self.service,
            'getAllOptions',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package.Server.Option import Option
        return SL_Option(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Server_Option':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Server.Option import Option
        return SL_Option(data)

# This file was automatically generated with tools/generateTypes.py
    def getOptions(
        self,
        type: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package_Server_Option]':
        data = self.client.call(
            self.service,
            'getOptions',
            type,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package.Server.Option import Option
        return SL_Option(data)


