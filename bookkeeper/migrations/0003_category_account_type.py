# Generated by Django 4.1.6 on 2023-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0002_category_color_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='account_type',
            field=models.CharField(choices=[('Asset/Expense', 'increase_debit'), ('Liabilitis/Income/Capital', 'increase_credit')], default='increase_debit', max_length=40),
        ),
    ]