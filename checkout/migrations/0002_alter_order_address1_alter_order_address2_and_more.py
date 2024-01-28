# Generated by Django 5.0 on 2024-01-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]