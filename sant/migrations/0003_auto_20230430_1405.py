# Generated by Django 3.1.13 on 2023-04-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sant', '0002_report_laborer_report_lamount_report_lrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='invoice_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
