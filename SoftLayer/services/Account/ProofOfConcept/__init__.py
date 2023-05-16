# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_ProofOfConcept(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_ProofOfConcept'
        self.client = client

    def approveReview(
        self,
        requestId: int,
        accessToken: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'approveReview',
            requestId,
            accessToken
        )
        
        return data


    def denyReview(
        self,
        requestId: int,
        accessToken: str,
        reason: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'denyReview',
            requestId,
            accessToken,
            reason
        )
        
        return data


    def getAuthenticationUrl(
        self,
        targetPage: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAuthenticationUrl',
            targetPage
        )
        
        return data


    def getRequestsPendingIntegratedOfferingTeamReview(
        self,
        accessToken: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Account_ProofOfConcept_Review_Summary]':

        data = self.client.call(
            self.service,
            'getRequestsPendingIntegratedOfferingTeamReview',
            accessToken,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return Summary(data)


    def getRequestsPendingOverThresholdReview(
        self,
        accessToken: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Account_ProofOfConcept_Review_Summary]':

        data = self.client.call(
            self.service,
            'getRequestsPendingOverThresholdReview',
            accessToken,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return Summary(data)


    def getReviewerAccessToken(
        self,
        unverifiedAuthenticationCode: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReviewerAccessToken',
            unverifiedAuthenticationCode
        )
        
        return data


    def getReviewerEmailFromAccessToken(
        self,
        accessToken: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReviewerEmailFromAccessToken',
            accessToken
        )
        
        return data


    def getSubmittedRequest(
        self,
        requestId: int
    ) -> 'SoftLayer_Container_Account_ProofOfConcept_Review':

        data = self.client.call(
            self.service,
            'getSubmittedRequest',
            requestId
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review import Review
        return Review(data)


    def getSubmittedRequests(
        self,
        email: str,
        sortOrder: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Account_ProofOfConcept_Review_Summary]':

        data = self.client.call(
            self.service,
            'getSubmittedRequests',
            email,
            sortOrder,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return Summary(data)


    def getSupportEmailAddress(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportEmailAddress',
            
        )
        
        return data


    def getTotalRequestsPendingIntegratedOfferingTeamReview(
        self,
        accessToken: str
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getTotalRequestsPendingIntegratedOfferingTeamReview',
            accessToken
        )
        
        return data


    def getTotalRequestsPendingOverThresholdReviewCount(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getTotalRequestsPendingOverThresholdReviewCount',
            
        )
        
        return data


    def isCurrentReviewer(
        self,
        requestId: int,
        accessToken: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isCurrentReviewer',
            requestId,
            accessToken
        )
        
        return data


    def isIntegratedOfferingTeamReviewer(
        self,
        emailAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isIntegratedOfferingTeamReviewer',
            emailAddress
        )
        
        return data


    def isOverThresholdReviewer(
        self,
        emailAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isOverThresholdReviewer',
            emailAddress
        )
        
        return data


    def requestAccountTeamFundedAccount(
        self,
        request: 'SoftLayer_Container_Account_ProofOfConcept_Request_AccountFunded'
    ) -> 'SoftLayer_Container_Account_ProofOfConcept_Review_Summary':

        data = self.client.call(
            self.service,
            'requestAccountTeamFundedAccount',
            request
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return Summary(data)


    def requestGlobalFundedAccount(
        self,
        request: 'SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded'
    ) -> 'SoftLayer_Container_Account_ProofOfConcept_Review_Summary':

        data = self.client.call(
            self.service,
            'requestGlobalFundedAccount',
            request
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return Summary(data)


    def verifyReviewer(
        self,
        requestId: int,
        reviewerEmailAddress: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'verifyReviewer',
            requestId,
            reviewerEmailAddress
        )
        
        return data


