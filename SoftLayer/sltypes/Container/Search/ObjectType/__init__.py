from SoftLayer.sltypes.Container.Search.ObjectType.Property import Container_Search_ObjectType_Property
from SoftLayer.sltypes.Entity import Entity

class Container_Search_ObjectType(Entity):
    """This data type is a container that stores information about a single indexed object type.  Object type
information can be used for discovery of searchable data and for creation or validation of object index
search strings.  Each of these containers holds a collection of
<b>[[SoftLayer_Container_Search_ObjectType_Property
(type)|SoftLayer_Container_Search_ObjectType_Property]]</b> objects, specifying which object properties are
exposed for the current user.  Refer to the the documentation for the
<b>[[SoftLayer_Search/search|search()]]</b> method for information on using object types in search strings."""
    name: str
    properties: list[Container_Search_ObjectType_Property]
