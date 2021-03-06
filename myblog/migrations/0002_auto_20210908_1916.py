# Generated by Django 3.2.6 on 2021-09-08 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('category_details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myblog.blogcategory'),
        ),
    ]
