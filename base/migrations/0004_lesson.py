# Generated by Django 4.2.7 on 2024-01-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('progress', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lessonReferenceNumber', models.IntegerField()),
            ],
        ),
    ]