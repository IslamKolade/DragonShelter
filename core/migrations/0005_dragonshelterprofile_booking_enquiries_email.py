# Generated by Django 4.2.6 on 2023-10-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "core",
            "0004_rename_description_dragonshelterprofile_short_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="dragonshelterprofile",
            name="booking_enquiries_email",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
