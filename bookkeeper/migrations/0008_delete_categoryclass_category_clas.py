# Generated by Django 4.1.6 on 2023-11-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0007_categoryclass_remove_transaction_amount_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryClass',
        ),
        migrations.AddField(
            model_name='category',
            name='clas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
