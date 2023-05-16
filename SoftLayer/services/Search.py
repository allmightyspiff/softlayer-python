# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Search(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Search'
        self.client = client

    def advancedSearch(
        self,
        searchString: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Container_Search_Result]':

        data = self.client.call(
            self.service,
            'advancedSearch',
            searchString,
            mask=objectMask
        )
        from SoftLayer.datatypes.Container.Search.Result import Result
        return Result(data)


    def getObjectTypes(
        self,
        
    ) -> 'list[SoftLayer_Container_Search_ObjectType]':

        data = self.client.call(
            self.service,
            'getObjectTypes',
            
        )
        from SoftLayer.datatypes.Container.Search.ObjectType import ObjectType
        return ObjectType(data)


    def search(
        self,
        searchString: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Container_Search_Result]':

        data = self.client.call(
            self.service,
            'search',
            searchString,
            mask=objectMask
        )
        from SoftLayer.datatypes.Container.Search.Result import Result
        return Result(data)


