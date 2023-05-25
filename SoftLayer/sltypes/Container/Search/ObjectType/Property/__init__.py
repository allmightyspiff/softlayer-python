from SoftLayer.sltypes.Entity import Entity

class Container_Search_ObjectType_Property(Entity):
    """This data type is a container that stores information about a single property of a searchable object type.
Each <b>[[SoftLayer_Container_Search_ObjectType (type)|SoftLayer_Container_Search_ObjectType]]</b> object
holds a collection of these properties.  Property information can be used for discovery of searchable data
and for the creation or validation of object index search strings.  Note that properties are only understood
by the <b>[[SoftLayer_Search/advancedSearch|advancedSearch()]]</b> method.  Refer to the
<b>advancedSearch()</b> method for information on using properties in search strings."""
    name: str
    sortableFlag: bool
    type_: str
