# Generated by Django 4.1 on 2023-03-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('super_user', 'super_user'), ('university_admin', 'university_admin'), ('university_user', 'university_user')], max_length=25),
        ),
    ]
