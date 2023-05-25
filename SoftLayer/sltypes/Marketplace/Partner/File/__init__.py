from SoftLayer.sltypes.Marketplace.Partner.File.Attributes import Marketplace_Partner_File_Attributes
from SoftLayer.sltypes.Entity import Entity

class Marketplace_Partner_File(Entity):
    attributes: Marketplace_Partner_File_Attributes
    contents: str
