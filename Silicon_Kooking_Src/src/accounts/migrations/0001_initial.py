# Generated by Django 2.0 on 2018-02-16 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(db_column='recipe', on_delete=django.db.models.deletion.PROTECT, to='recipes.Recipe')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favorite',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('recipe', 'user')},
        ),
    ]
