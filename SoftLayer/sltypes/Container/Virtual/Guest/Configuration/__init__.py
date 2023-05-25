from SoftLayer.sltypes.Container.Virtual.Guest.Configuration.Option import Container_Virtual_Guest_Configuration_Option
from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_Guest_Configuration(Entity):
    """The guest configuration container is used to provide configuration options for creating computing instances.
Each configuration option will include both an <code>itemPrice</code> and a <code>template</code>.   The
<code>itemPrice</code> value will provide hourly and monthly costs (if either are applicable), and a
description of the option.   The <code>template</code> will provide a fragment of the request with the
properties and values that must be sent when creating a computing instance with the option.   The
[[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] method returns this data structure.
<style type="text/css">#properties .views-field-body p { margin-top: 1.5em; };</style>"""
    blockDevices: list[Container_Virtual_Guest_Configuration_Option]
    datacenters: list[Container_Virtual_Guest_Configuration_Option]
    flavors: list[Container_Virtual_Guest_Configuration_Option]
    memory: list[Container_Virtual_Guest_Configuration_Option]
    networkComponents: list[Container_Virtual_Guest_Configuration_Option]
    operatingSystems: list[Container_Virtual_Guest_Configuration_Option]
    processors: list[Container_Virtual_Guest_Configuration_Option]
