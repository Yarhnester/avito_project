# Generated by Django 3.2.16 on 2022-10-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='absent',
        ),
        migrations.RemoveField(
            model_name='record',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='record',
            name='the_copy',
        ),
        migrations.RemoveField(
            model_name='record',
            name='the_original',
        ),
        migrations.RemoveField(
            model_name='record',
            name='title',
        ),
        migrations.AddField(
            model_name='record',
            name='contact',
            field=models.CharField(blank=True, max_length=150, verbose_name='Контактное лицо'),
        ),
        migrations.AddField(
            model_name='record',
            name='partner',
            field=models.CharField(blank=True, max_length=150, verbose_name='Контрагент'),
        ),
        migrations.AddField(
            model_name='record',
            name='the_original_contract',
            field=models.CharField(blank=True, choices=[('Original', 'Оригинал'), ('Copy', 'Копия'), ('Absent', 'Отсутствует'), ('Not needed', 'Не нужен')], default='Not needed', max_length=10, verbose_name='Статус договора'),
        ),
        migrations.AlterField(
            model_name='record',
            name='document',
            field=models.CharField(blank=True, max_length=150, verbose_name='Доставка документов'),
        ),
        migrations.AlterField(
            model_name='record',
            name='edo',
            field=models.CharField(blank=True, choices=[('Yes', 'Да'), ('No', 'Нет')], default='No', max_length=3, verbose_name='ЭДО'),
        ),
        migrations.AlterField(
            model_name='record',
            name='notes',
            field=models.TextField(blank=True, max_length=250, verbose_name='Примечания'),
        ),
        migrations.AlterField(
            model_name='record',
            name='payment_date',
            field=models.DateField(verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='record',
            name='pvz',
            field=models.CharField(blank=True, choices=[('PVZ1', 'ПВЗ-1'), ('PVZ2', 'ПВЗ-2'), ('PVZ3', 'ПВЗ-3'), ('PVZ4', 'ПВЗ-4'), ('PVZ5', 'ПВЗ-5'), ('PVZ6', 'ПВЗ-6'), ('PVZ7', 'ПВЗ-7'), ('PVZ8', 'ПВЗ-8')], default=None, max_length=4, verbose_name='ПВЗ'),
        ),
        migrations.AlterField(
            model_name='record',
            name='rate',
            field=models.IntegerField(blank=True, verbose_name='Тариф'),
        ),
        migrations.AlterField(
            model_name='record',
            name='service',
            field=models.CharField(blank=True, max_length=50, verbose_name='Услуга'),
        ),
    ]