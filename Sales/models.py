from django.db import models

class OutwardChallan(models.Model):
    Plant = models.CharField(max_length=100, blank=True, null=True)
    Series = models.CharField(max_length=100, blank=True, null=True)
    Vendor = models.CharField(max_length=100, blank=True, null=True)
    challan_no = models.CharField(max_length=100, blank=True, null=True)  # e.g., F6252600001
    challan_date = models.CharField(max_length=100, blank=True, null=True)
    challan_time = models.CharField(max_length=100, blank=True, null=True)
    DcNo = models.CharField(max_length=100, blank=True, null=True)
    transport_name = models.CharField(max_length=100, blank=True, null=True)
    vehicle_no = models.CharField(max_length=100, blank=True, null=True)
    estimated_value = models.CharField(max_length=100, blank=True, null=True)
    DcDate = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_no = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_date = models.CharField(max_length=100, blank=True, null=True)
    rev_charges = models.CharField(max_length=100, blank=True, null=True)
    rev_charges_amount = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_qty = models.CharField(max_length=100, blank=True, null=True)
    remarknote = models.CharField(max_length=100, blank=True, null=True)
    ship_to_add_code = models.CharField(max_length=100, blank=True, null=True)
    challan_due_date = models.CharField(max_length=100, blank=True, null=True)
    SelectWorkOrder = models.CharField(max_length=100, blank=True, null=True)
    assessable_value = models.CharField(max_length=100, blank=True, null=True)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    igst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    lr_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"Challan {self.challan_no} - {self.vendor_name}"