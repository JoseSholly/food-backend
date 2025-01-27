# Generated by Django 4.2.16 on 2025-01-26 16:26

from django.db import migrations, models
import user.utils


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_activity_level_user_age_user_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dietary_restrictions',
            field=models.JSONField(blank=True, default=list, help_text='Dietary restrictions of user', validators=[user.utils.validate_dietary_restrictions]),
        ),
    ]
