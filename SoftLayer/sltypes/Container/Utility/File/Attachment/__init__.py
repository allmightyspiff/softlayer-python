from SoftLayer.sltypes.Entity import Entity

class Container_Utility_File_Attachment(Entity):
    """At times,such as when attaching files to tickets, it is necessary to send files to SoftLayer API methods. The
SoftLayer_Container_Utility_File_Attachment data type models a single file to upload to the API."""
    data: str
    filename: str
