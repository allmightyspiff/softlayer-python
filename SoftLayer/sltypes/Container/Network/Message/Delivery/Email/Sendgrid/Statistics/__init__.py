from SoftLayer.sltypes.Entity import Entity

class Container_Network_Message_Delivery_Email_Sendgrid_Statistics(Entity):
    blocks: int
    bounces: int
    clicks: int
    date: str
    delivered: int
    invalidEmail: int
    opens: int
    repeatBounces: int
    repeatSpamReports: int
    repeatUnsubscribes: int
    requests: int
    spamReports: int
    uniqueClicks: int
    uniqueOpens: int
    unsubscribes: int
