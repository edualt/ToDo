# Generated by Django 4.0.1 on 2022-02-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_images_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='task',
            name='photo',
            field=models.ImageField(null=True, upload_to='myimage'),
        ),
    ]
