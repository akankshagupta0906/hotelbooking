# Generated by Django 2.1.7 on 2021-07-09 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HotelBooking', '0001_initial'),
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinghotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(default='0', max_length=100)),
                ('total_amt', models.IntegerField(default=0)),
                ('amtstatus', models.IntegerField(default=0)),
                ('start_day', models.CharField(default=-1997, max_length=20)),
                ('end_day', models.CharField(default=-1997, max_length=20)),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('roomqty', models.IntegerField(default=0)),
                ('guests', models.IntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.City')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelBooking.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Cancel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=30)),
                ('canceldate', models.DateField(auto_now=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelBooking.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelBooking.UserProfile')),
            ],
        ),
    ]
