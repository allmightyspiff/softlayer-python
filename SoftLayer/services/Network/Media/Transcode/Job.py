# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Media_Transcode_Job(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Media_Transcode_Job'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Media_Transcode_Job,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Job':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job import Job
        return Job(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Job':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job import Job
        return Job(data)


    def getHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Media_Transcode_Job_History]':

        data = self.client.call(
            self.service,
            'getHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job.History import History
        return History(data)


    def getTranscodeAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Account':

        data = self.client.call(
            self.service,
            'getTranscodeAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Account import Account
        return Account(data)


    def getTranscodeStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Job_Status':

        data = self.client.call(
            self.service,
            'getTranscodeStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job.Status import Status
        return Status(data)


    def getTranscodeStatusName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTranscodeStatusName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


