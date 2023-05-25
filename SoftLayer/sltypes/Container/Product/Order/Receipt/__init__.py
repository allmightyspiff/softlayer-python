from SoftLayer.sltypes.Billing.Order.Quote import Billing_Order_Quote
from SoftLayer.sltypes.Billing.Order import Billing_Order
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Receipt(Entity):
    """When an order is placed (SoftLayer_Product_Order::placeOrder), a receipt is returned when the order is
created successfully. The information in the receipt helps explain information about the order. It's order
ID, and all the data within the order as well.   For PayPal Orders, an URL is also returned to the user so
that the user can complete the transaction. Users paying with PayPal must continue on to this URL, login and
pay. When doing this, PayPal will redirect the user back to a SoftLayer page which will then "finalize" the
authorization process. From here, Sales will verify the order by contacting the user in some way, unless
sales has already spoken to the user about approving the order.   For users paying with a credit card, a
receipt means the order has gone to sales and is awaiting approval."""
    externalPaymentCheckoutUrl: str
    externalPaymentToken: str
    orderDate: datetime
    orderDetails: Container_Product_Order
    orderId: int
    paypalCheckoutUrl: str
    paypalToken: str
    placedOrder: Billing_Order
    quote: Billing_Order_Quote
