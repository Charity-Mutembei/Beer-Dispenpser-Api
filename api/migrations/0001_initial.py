# Generated by Django 4.1 on 2022-11-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensing_status', models.CharField(choices=[('open', 'open'), ('close', 'close')], max_length=200)),
                ('productname', models.CharField(choices=[('Larger beer', 'Larger beer'), ('Pilsner beer', 'Pilsner beer'), ('Guness beer', 'Guness beer')], max_length=300)),
                ('flow_volume', models.DecimalField(decimal_places=3, default=0.065, max_digits=100)),
                ('price', models.DecimalField(decimal_places=2, default=2.0, max_digits=15)),
                ('dispensing_time', models.TimeField()),
                ('stop_dispensing_time', models.TimeField()),
            ],
        ),
    ]