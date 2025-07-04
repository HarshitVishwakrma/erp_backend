# Generated by Django 5.0.6 on 2025-04-02 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DC_GRN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GrnNo', models.CharField(blank=True, max_length=255, null=True)),
                ('GrnDate', models.CharField(blank=True, max_length=255, null=True)),
                ('GrnTime', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.DateField()),
                ('InvoiceNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceDate', models.DateField()),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('PreparedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('CheckedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('DeliveryInTime', models.BooleanField(default=True)),
                ('QcCheck', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryChallan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SelectItem', models.CharField(blank=True, max_length=255, null=True)),
                ('Store', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemCode', models.CharField(blank=True, max_length=255, null=True)),
                ('HSNCode', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Purpose', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, max_length=255, null=True)),
                ('Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant', models.CharField(blank=True, max_length=255, null=True)),
                ('Series', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Supp_Cust', models.CharField(blank=True, max_length=255, null=True)),
                ('GE_No', models.CharField(blank=True, max_length=255, null=True)),
                ('GE_Date', models.CharField(blank=True, max_length=255, null=True)),
                ('GE_Time', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.DateField()),
                ('Select', models.CharField(blank=True, max_length=255, null=True)),
                ('InVoiceNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Invoicedate', models.DateField()),
                ('EWayBillNo', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillDate', models.DateField()),
                ('ContactPerson', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrnGenralDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant', models.CharField(blank=True, max_length=255, null=True)),
                ('Series', models.CharField(blank=True, max_length=255, null=True)),
                ('GateEntryNo', models.CharField(blank=True, max_length=255, null=True)),
                ('SelectSupplier', models.CharField(blank=True, max_length=255, null=True)),
                ('SelectPO', models.CharField(blank=True, max_length=255, null=True)),
                ('AddChallanGrnQty', models.BooleanField(default=False)),
                ('SelectItem', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemDropdown', models.CharField(blank=True, max_length=255, null=True)),
                ('HeatNo', models.CharField(blank=True, max_length=255, null=True)),
                ('GrnNo', models.CharField(blank=True, max_length=255, null=True)),
                ('GrnDate', models.CharField(blank=True, max_length=255, null=True)),
                ('GrnTime', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceDate', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillNo', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillDate', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('PreparedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('CheckedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('TcNo', models.CharField(blank=True, max_length=255, null=True)),
                ('TcDate', models.CharField(blank=True, max_length=255, null=True)),
                ('QcCheck', models.BooleanField(default=False)),
                ('Delivery', models.BooleanField(default=False)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('PaymentTermDay', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InwardChallan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InwardF4No', models.CharField(blank=True, max_length=255, null=True)),
                ('InwardDate', models.CharField(blank=True, max_length=255, null=True)),
                ('InwardTime', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.DateField()),
                ('GateEnrtyNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceDate', models.DateField()),
                ('EWayBillQty', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillNo', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('PreparedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('CheckedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('TcNo', models.CharField(blank=True, max_length=255, null=True)),
                ('TcDate', models.DateField()),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('DeliveryInTime', models.BooleanField(default=True)),
                ('TotalItem', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalQtyNo', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalQtyKg', models.CharField(blank=True, max_length=255, null=True)),
                ('Store', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InwardF4No', models.CharField(blank=True, max_length=255, null=True)),
                ('InwardDate', models.CharField(blank=True, max_length=255, null=True)),
                ('InwardTime', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.DateField()),
                ('SubVendor', models.CharField(blank=True, max_length=255, null=True)),
                ('DcNo', models.CharField(blank=True, max_length=255, null=True)),
                ('DcDate', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillQty', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillNo', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('PreparedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('CheckedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleTime', models.CharField(blank=True, max_length=255, null=True)),
                ('TcNo', models.CharField(blank=True, max_length=255, null=True)),
                ('TcDate', models.DateField()),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('DeliveryInTime', models.BooleanField(default=True)),
                ('ClearingStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleOutTime', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Issue_General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemDescription', models.CharField(blank=True, max_length=255, null=True)),
                ('AvailableStock', models.CharField(blank=True, max_length=255, null=True)),
                ('StockStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('Machine', models.CharField(blank=True, max_length=255, null=True)),
                ('StoreName', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('MrnNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemDescription', models.CharField(blank=True, max_length=255, null=True)),
                ('AvailableStock', models.CharField(blank=True, max_length=255, null=True)),
                ('Machine', models.CharField(blank=True, max_length=255, null=True)),
                ('StoreName', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('MrnNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New_Indent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SelectItem', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Available', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, max_length=255, null=True)),
                ('Machine', models.CharField(blank=True, max_length=255, null=True)),
                ('Department', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('UseFor', models.CharField(blank=True, max_length=255, null=True)),
                ('MoRef', models.CharField(blank=True, max_length=255, null=True)),
                ('SchDate', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewMrn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant', models.CharField(blank=True, max_length=255, null=True)),
                ('Series', models.CharField(blank=True, max_length=255, null=True)),
                ('MRN_no', models.CharField(blank=True, max_length=255, null=True)),
                ('General', models.BooleanField(default=False)),
                ('Work_order', models.BooleanField(default=False)),
                ('ItemCode', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty_1', models.CharField(blank=True, max_length=255, null=True)),
                ('QtyUnit', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Machine', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee', models.CharField(blank=True, max_length=255, null=True)),
                ('Dept', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark_1', models.CharField(blank=True, max_length=255, null=True)),
                ('MRN_date', models.CharField(blank=True, max_length=255, null=True)),
                ('MRN_time', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark_2', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondDeliveryChallan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Contractor', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanDate', models.DateField()),
                ('Transport', models.CharField(blank=True, max_length=255, null=True)),
                ('EWayBillNo', models.CharField(blank=True, max_length=255, null=True)),
                ('PoNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Ref_Person', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('PoDate', models.CharField(blank=True, max_length=255, null=True)),
                ('Department', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('AssessableValue', models.CharField(blank=True, max_length=255, null=True)),
                ('CGST', models.CharField(blank=True, max_length=255, null=True)),
                ('SGST', models.CharField(blank=True, max_length=255, null=True)),
                ('IGST', models.CharField(blank=True, max_length=255, null=True)),
                ('GrandTotal', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondNew_Indent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPCCode', models.CharField(blank=True, max_length=255, null=True)),
                ('WorkOrder', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InWardNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InWardDate', models.DateField()),
                ('InWardTime', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallanNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ChallonDate', models.DateField()),
                ('GIN_No', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceNo', models.CharField(blank=True, max_length=255, null=True)),
                ('InvoiceDate', models.DateField()),
                ('PreparedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('CheckedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('VehicleNo', models.CharField(blank=True, max_length=255, null=True)),
                ('LrNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Transporter', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('DeliveryInTime', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GrnGst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.CharField(blank=True, max_length=255, null=True)),
                ('HSN', models.CharField(blank=True, max_length=255, null=True)),
                ('PoRate', models.CharField(blank=True, max_length=255, null=True)),
                ('DiscRate', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty', models.CharField(blank=True, max_length=255, null=True)),
                ('Discount', models.CharField(blank=True, max_length=255, null=True)),
                ('PackAmt', models.CharField(blank=True, max_length=255, null=True)),
                ('TransAmt', models.CharField(blank=True, max_length=255, null=True)),
                ('AssValue', models.CharField(blank=True, max_length=255, null=True)),
                ('CGST', models.CharField(blank=True, max_length=255, null=True)),
                ('SGST', models.CharField(blank=True, max_length=255, null=True)),
                ('IGST', models.CharField(blank=True, max_length=255, null=True)),
                ('VAT', models.CharField(blank=True, max_length=255, null=True)),
                ('CESS', models.CharField(blank=True, max_length=255, null=True)),
                ('New_MRN_Detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GrnGst', to='Store.grngenraldetail')),
            ],
        ),
        migrations.CreateModel(
            name='GrnGstTDC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessable_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('packing_forwarding_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transport_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('insurance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('installation_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('other_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Tds', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sgst', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('igst', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cess_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tcs_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('New_MRN_Detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GrnGstTDC', to='Store.grngenraldetail')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty_NOS', models.CharField(blank=True, max_length=255, null=True)),
                ('QTY_KG', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit_Code', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark', models.CharField(blank=True, max_length=255, null=True)),
                ('Work_Order_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItemDetails', to='Store.generaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField()),
                ('part_no', models.CharField(max_length=100, unique=True)),
                ('item_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.itemgroup')),
                ('main_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.maingroup')),
            ],
        ),
        migrations.CreateModel(
            name='NewMRNTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('QtyUnit', models.CharField(blank=True, max_length=255, null=True)),
                ('Qty_1', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Machine', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee', models.CharField(blank=True, max_length=255, null=True)),
                ('Dept', models.CharField(blank=True, max_length=255, null=True)),
                ('Remark_1', models.CharField(blank=True, max_length=255, null=True)),
                ('New_MRN_Detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NewMRNTable', to='Store.newmrn')),
            ],
        ),
        migrations.CreateModel(
            name='RefTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemDesc', models.CharField(blank=True, max_length=255, null=True)),
                ('MillTcName', models.CharField(blank=True, max_length=255, null=True)),
                ('MillTcNo', models.CharField(blank=True, max_length=255, null=True)),
                ('MillTcDate', models.CharField(blank=True, max_length=255, null=True)),
                ('Location', models.CharField(blank=True, max_length=255, null=True)),
                ('New_MRN_Detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RefTC', to='Store.grngenraldetail')),
            ],
        ),
    ]
