# Generated by Django 3.0.5 on 2020-04-24 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cr_date', models.DateTimeField(auto_now_add=True, verbose_name='дататайм создания ')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='дататайм отправки')),
                ('client', models.ForeignKey(blank=True, help_text='анкета', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lists.Form')),
                ('status', models.ForeignKey(blank=True, help_text='статус', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lists.Status')),
                ('types', models.ForeignKey(blank=True, help_text='тип предложения', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lists.OfferTypes')),
            ],
            options={
                'verbose_name': 'заявка',
                'verbose_name_plural': 'заявки',
                'managed': True,
            },
        ),
    ]