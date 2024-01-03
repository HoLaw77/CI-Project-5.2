# Generated by Django 5.0 on 2024-01-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Romance fiction'), (2, 'Thriller fiction'), (3, 'Detective fiction'), (4, 'Classic'), (5, 'Nonfiction'), (6, 'Sci-fi/Fantasy'), (7, 'Poetry'), (8, 'Science'), (9, 'Social Science'), (10, 'Philosophy'), (11, 'Gender'), (12, 'Translated Fiction'), (13, 'Literary Fiction')], default=1),
        ),
    ]
