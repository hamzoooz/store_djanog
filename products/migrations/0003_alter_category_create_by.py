# Generated by Django 4.2.4 on 2023-08-28 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_producs_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.profile'),
        ),
    ]
