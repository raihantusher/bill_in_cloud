# Generated by Django 4.1.6 on 2023-05-05 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_alter_expenseslist_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='expense.category'),
        ),
    ]