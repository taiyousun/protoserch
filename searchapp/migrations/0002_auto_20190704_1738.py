# Generated by Django 2.1.9 on 2019-07-04 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodstbl',
            name='categoryid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='searchapp.CategoryTBL'),
        ),
    ]