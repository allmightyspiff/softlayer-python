from datetime import datetime
from SoftLayer.sltypes.Dns.Domain.Registration.Registrant.Verification.Status import Dns_Domain_Registration_Registrant_Verification_Status
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail(Entity):
    status: Dns_Domain_Registration_Registrant_Verification_Status
    verificationDeadlineDate: datetime
