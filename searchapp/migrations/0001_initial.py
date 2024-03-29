# Generated by Django 2.1.9 on 2019-07-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTBL',
            fields=[
                ('categoryid', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='カテゴリID')),
                ('highcategoryid', models.CharField(max_length=12, verbose_name='上位カテゴリID')),
                ('categoryname', models.CharField(max_length=15, verbose_name='カテゴリ名')),
            ],
            options={
                'db_table': 'categorytbl',
            },
        ),
        migrations.CreateModel(
            name='GoodsTBL',
            fields=[
                ('goodsid', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='商品ID')),
                ('categoryid', models.CharField(max_length=12, verbose_name='カテゴリID')),
                ('sizename', models.CharField(max_length=1, verbose_name='サイズ')),
                ('colorname', models.CharField(max_length=15, verbose_name='色')),
                ('goodsname', models.CharField(max_length=70, verbose_name='商品名')),
                ('goodsdescription', models.CharField(max_length=150, verbose_name='商品記述')),
                ('goodsurl', models.URLField(max_length=100, verbose_name='商品画像URL')),
                ('price', models.IntegerField(verbose_name='価格')),
                ('goodsstocks', models.IntegerField(verbose_name='在庫数')),
                ('salesstartdate', models.DateField(verbose_name='販売開始年月日')),
                ('salesenddate', models.DateField(verbose_name='販売終了年月日')),
                ('entrydate', models.DateTimeField(verbose_name='登録年月日時分秒')),
                ('updatedate', models.DateTimeField(verbose_name='更新年月日時分秒')),
                ('deleteflag', models.IntegerField(default='1', verbose_name='論理削除フラグ')),
            ],
            options={
                'db_table': 'goodstbl',
            },
        ),
    ]
