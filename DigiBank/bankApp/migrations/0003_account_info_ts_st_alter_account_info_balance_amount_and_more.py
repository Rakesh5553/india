# Generated by Django 4.2.1 on 2023-09-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankApp', '0002_account_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_info',
            name='ts_st',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='account_info',
            name='balance_amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account_info',
            name='deposit_amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account_info',
            name='withdraw_amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Master_Account',
            fields=[
                ('ms_id', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('deposit_amount', models.BigIntegerField(default=0)),
                ('master_balance', models.BigIntegerField(default=0)),
                ('withdraw_amount', models.BigIntegerField(default=0)),
                ('ts_dt', models.DateTimeField(auto_now_add=True)),
                ('account_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankApp.cust_info')),
            ],
        ),
    ]
