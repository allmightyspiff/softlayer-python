# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Component_Locator(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Component_Locator'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getGenericComponentModelAvailability(
        self,
        genericComponentModelIds: int
    ) -> 'list[SoftLayer_Hardware_Component_Locator_Result]':
        data = self.client.call(
            self.service,
            'getGenericComponentModelAvailability',
            genericComponentModelIds
        )
        from SoftLayer.datatypes.Hardware.Component.Locator.Result import Result
        return SL_Result(data)

# This file was automatically generated with tools/generateTypes.py
    def getPackageItemsAvailability(
        self,
        packageId: int
    ) -> 'list[SoftLayer_Hardware_Component_Locator_Result]':
        data = self.client.call(
            self.service,
            'getPackageItemsAvailability',
            packageId
        )
        from SoftLayer.datatypes.Hardware.Component.Locator.Result import Result
        return SL_Result(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerPackageAvailability(
        self,
        
    ) -> 'list[SoftLayer_Hardware_Component_Locator_Result]':
        data = self.client.call(
            self.service,
            'getServerPackageAvailability',
            
        )
        from SoftLayer.datatypes.Hardware.Component.Locator.Result import Result
        return SL_Result(data)


