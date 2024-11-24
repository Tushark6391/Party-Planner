# Generated by Django 4.1.7 on 2023-10-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
