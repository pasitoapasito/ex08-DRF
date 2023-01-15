# Generated by Django 3.2.14 on 2023-01-15 20:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'coupons',
            },
        ),
    ]
