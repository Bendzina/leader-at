# Generated by Django 5.1.2 on 2024-12-24 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_height_product_length_product_weight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='storeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.store'),
        ),
    ]
