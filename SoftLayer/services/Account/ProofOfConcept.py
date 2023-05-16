# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_ProofOfConcept(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_ProofOfConcept'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Review(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getSupportEmailAddress(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getSupportEmailAddress',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getTotalRequestsPendingOverThresholdReviewCount(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getTotalRequestsPendingOverThresholdReviewCount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def requestAccountTeamFundedAccount(
        self,
        request: SoftLayer_Container_Account_ProofOfConcept_Request_AccountFunded
    ) -> 'SoftLayer_Container_Account_ProofOfConcept_Review_Summary':
        data = self.client.call(
            self.service,
            'requestAccountTeamFundedAccount',
            request
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def requestGlobalFundedAccount(
        self,
        request: SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded
    ) -> 'SoftLayer_Container_Account_ProofOfConcept_Review_Summary':
        data = self.client.call(
            self.service,
            'requestGlobalFundedAccount',
            request
        )
        from SoftLayer.datatypes.Container.Account.ProofOfConcept.Review.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
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


