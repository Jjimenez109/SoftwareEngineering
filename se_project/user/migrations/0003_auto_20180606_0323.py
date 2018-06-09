# Generated by Django 2.0.5 on 2018-06-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180602_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='C_card_number',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='Exp_day',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='Exp_month',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='purchase_history_content',
            name='Time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reserved_credit_card',
            name='RCC_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]