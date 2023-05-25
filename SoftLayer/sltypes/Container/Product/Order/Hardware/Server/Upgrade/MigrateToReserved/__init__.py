from datetime import datetime
from SoftLayer.sltypes.Container.Product.Order.Hardware.Server.Upgrade import Container_Product_Order_Hardware_Server_Upgrade
from SoftLayer.sltypes.Container_Product_Order_Hardware_Server_Upgrade import Container_Product_Order_Hardware_Server_Upgrade

class Container_Product_Order_Hardware_Server_Upgrade_MigrateToReserved(Container_Product_Order_Hardware_Server_Upgrade):
    """Use this datatype to upgrade your existing monthly-billed server to term based pricing. Only monthly to 1
year, and 1 year to 3 year migrations are available. A new billing agreement contract will be created upon
order approval, starting at the next billing cycle. A price is required for each existing billing item and
all term-based prices must match in length. Hourly billed servers are not eligible for this upgrade.
Downgrading to a shorter term is not available. Multiple term upgrades per billing cycle are not allowed."""
    termLength: int
    termStartDate: datetime
