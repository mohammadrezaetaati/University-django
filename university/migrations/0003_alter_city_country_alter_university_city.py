# Generated by Django 4.1.3 on 2022-11-13 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("university", "0002_alter_university_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="university.country"
            ),
        ),
        migrations.AlterField(
            model_name="university",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="university.city"
            ),
        ),
    ]
