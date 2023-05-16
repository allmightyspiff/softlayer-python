# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Media_Transcode_Job_Status(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Media_Transcode_Job_Status'
        self.client = client

    def getAllStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Media_Transcode_Job_Status]':

        data = self.client.call(
            self.service,
            'getAllStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job.Status import Status
        return Status(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Job_Status':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job.Status import Status
        return Status(data)


