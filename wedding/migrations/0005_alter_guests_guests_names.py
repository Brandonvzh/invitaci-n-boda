# Generated by Django 4.2.6 on 2024-01-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_alter_guests_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='guests_names',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
