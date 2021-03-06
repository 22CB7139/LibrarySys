# Generated by Django 2.0 on 2018-05-04 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('title', models.CharField(max_length=200, verbose_name='书名')),
                ('subtitle', models.CharField(blank=True, max_length=200, verbose_name='副标题')),
                ('pages', models.IntegerField(blank=True, verbose_name='页数')),
                ('author', models.CharField(max_length=60, verbose_name='作者')),
                ('translator', models.CharField(blank=True, max_length=60, verbose_name='译者')),
                ('price', models.CharField(blank=True, max_length=60, verbose_name='定价')),
                ('publisher', models.CharField(blank=True, max_length=200, verbose_name='出版社')),
                ('pubdate', models.CharField(blank=True, max_length=60, verbose_name='出版日期')),
                ('cover_img', models.URLField(blank=True, verbose_name='封面图')),
                ('summary', models.TextField(blank=True, max_length=2000, verbose_name='内容简介')),
                ('author_intro', models.TextField(blank=True, max_length=2000, verbose_name='作者简介')),
                ('available', models.NullBooleanField(default=True, verbose_name='是否可借')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='入库时间')),
                ('borrow_date', models.DateField(blank=True, null=True, verbose_name='借阅日期')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='归还日期')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='借阅者')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
    ]
