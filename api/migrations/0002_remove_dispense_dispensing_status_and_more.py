# Generated by Django 4.1 on 2022-11-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispense',
            name='dispensing_status',
        ),
        migrations.RemoveField(
            model_name='dispense',
            name='flow_volume',
        ),
        migrations.AlterField(
            model_name='dispense',
            name='dispensing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dispense',
            name='productname',
            field=models.CharField(choices=[('Larger beer', 'Larger beer'), ('Pilsner beer', 'Pilsner beer'), ('Guness beer', 'Guness beer')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dispense',
            name='stop_dispensing_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
