from SoftLayer.sltypes.Entity import Entity

class Container_Billing_Invoice_Email(Entity):
    """This container is used to provide all the options for
[[SoftLayer_Billing_Invoice/emailInvoices|emailInvoices]] in order to have the necessary invoices generated
and links sent to the user's email."""
    excelInvoiceIds: list[int]
    pdfDetailedInvoiceIds: list[int]
    pdfInvoiceIds: list[int]
    type_: str
