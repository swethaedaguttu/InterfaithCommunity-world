# Generated by Django 5.1 on 2024-10-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_date_alter_event_rsvp_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnifiedNight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
