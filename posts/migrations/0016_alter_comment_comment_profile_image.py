# Generated by Django 3.2.13 on 2022-06-05 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_comment_comment_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comment_profile_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.profile'),
        ),
    ]
