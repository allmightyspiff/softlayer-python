from SoftLayer.sltypes.Entity import Entity

class Network_Security_Scanner_Request_Status(Entity):
    """The SoftLayer_Network_Security_Scanner_Request_Status data type represents the current status of a
vulnerability scan. The status messages are as follows:  *Scan Pending *Scan Processing *Scan Complete *Scan
Cancelled *Generating Report.   The status of a vulnerability scan will change over the course of a scan's
execution."""
    id_: int
    name: str
