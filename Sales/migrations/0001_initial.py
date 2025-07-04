# Generated by Django 5.2.3 on 2025-07-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutwardChallan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant', models.CharField(blank=True, max_length=100, null=True)),
                ('Series', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor', models.CharField(blank=True, max_length=100, null=True)),
                ('challan_no', models.CharField(blank=True, max_length=100, null=True)),
                ('challan_date', models.CharField(blank=True, max_length=100, null=True)),
                ('challan_time', models.CharField(blank=True, max_length=100, null=True)),
                ('DcNo', models.CharField(blank=True, max_length=100, null=True)),
                ('transport_name', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_no', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_value', models.CharField(blank=True, max_length=100, null=True)),
                ('DcDate', models.CharField(blank=True, max_length=100, null=True)),
                ('eway_bill_no', models.CharField(blank=True, max_length=100, null=True)),
                ('eway_bill_date', models.CharField(blank=True, max_length=100, null=True)),
                ('rev_charges', models.CharField(blank=True, max_length=100, null=True)),
                ('rev_charges_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('eway_bill_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('remarknote', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_to_add_code', models.CharField(blank=True, max_length=100, null=True)),
                ('challan_due_date', models.CharField(blank=True, max_length=100, null=True)),
                ('SelectWorkOrder', models.CharField(blank=True, max_length=100, null=True)),
                ('assessable_value', models.CharField(blank=True, max_length=100, null=True)),
                ('cgst', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sgst', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('igst', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('lr_no', models.CharField(blank=True, max_length=100, null=True)),
                ('lr_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
