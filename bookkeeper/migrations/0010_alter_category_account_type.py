# Generated by Django 4.1.6 on 2023-11-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0009_alter_category_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='account_type',
            field=models.CharField(choices=[('asset_expense', 'Asset/Expense'), ('liabilities_equity', 'Liabilities/Income/Capital')], default='asset_expense', max_length=40),
        ),
    ]