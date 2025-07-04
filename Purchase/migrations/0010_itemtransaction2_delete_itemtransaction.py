# Generated by Django 5.0.6 on 2025-05-22 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0009_remove_newjobworkpoinfo_item_details_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTransaction2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(max_length=100)),
                ('ItemDescription', models.CharField(max_length=255)),
                ('PartCode', models.CharField(max_length=100)),
                ('Out', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inn', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RType', models.CharField(max_length=50)),
                ('Disc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PoQty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Unit', models.CharField(max_length=50)),
                ('ParticularProcess', models.CharField(max_length=255)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.item')),
            ],
        ),
        migrations.DeleteModel(
            name='ItemTransaction',
        ),
    ]
