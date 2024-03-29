# Generated by Django 4.2.6 on 2023-10-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('num_guests_assigned', models.IntegerField(max_length=10)),
                ('num_guests_selected', models.IntegerField(max_length=10)),
                ('answer', models.CharField(choices=[('Sí asistiré', 'Sí asistiré'), ('No asistiré', 'No, asistiré')], default='Sí asistiré', max_length=100)),
                ('guests_names', models.CharField(max_length=250)),
                ('wish_text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
