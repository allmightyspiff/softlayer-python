from SoftLayer.sltypes.Container.Hardware.Configuration.Option import Container_Hardware_Configuration_Option
from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Configuration(Entity):
    """The hardware configuration container is used to provide configuration options for servers.   Each
configuration option will include both an <code>itemPrice</code> and a <code>template</code>.   The
<code>itemPrice</code> value will provide hourly and monthly costs (if either are applicable), and a
description of the option.   The <code>template</code> will provide a fragment of the request with the
properties and values that must be sent when creating a server with the option.   The
[[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] method returns this data structure.
<style type="text/css">#properties .views-field-body p { margin-top: 1.5em; };</style>"""
    datacenters: list[Container_Hardware_Configuration_Option]
    fixedConfigurationPresets: list[Container_Hardware_Configuration_Option]
    hardDrives: list[Container_Hardware_Configuration_Option]
    networkComponents: list[Container_Hardware_Configuration_Option]
    operatingSystems: list[Container_Hardware_Configuration_Option]
    processors: list[Container_Hardware_Configuration_Option]
