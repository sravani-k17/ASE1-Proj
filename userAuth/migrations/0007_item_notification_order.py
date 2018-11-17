# Generated by Django 2.1.2 on 2018-11-17 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0006_remove_agent_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50)),
                ('itemcost', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notifid', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=500)),
                ('seen', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifier', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notified_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('billingaddress', models.CharField(max_length=200)),
                ('billingdate', models.DateTimeField(auto_now_add=True)),
                ('billingamount', models.PositiveIntegerField(default=0)),
                ('orderplaced', models.BooleanField(default=False)),
                ('billingtype', models.CharField(choices=[('0', 'FAILED'), ('1', 'PLACED'), ('2', 'CONFIRMED'), ('3', 'OUT FOR DELIVERY'), ('4', 'DELIVERED')], max_length=1)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_agent', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]