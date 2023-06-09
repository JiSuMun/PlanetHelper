# Generated by Django 3.2.18 on 2023-06-15 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import secondhands.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='S_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('content', models.TextField()),
                ('city', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('road_address', models.CharField(max_length=100)),
                ('d_address', models.CharField(max_length=100)),
                ('extra_address', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('잡화', '잡화'), ('전자제품', '전자제품'), ('의류', '의류'), ('도서', '도서'), ('기타', '기타')], max_length=10)),
                ('status', models.CharField(choices=[('1', ''), ('2', '예약중'), ('3', '거래완료')], default='', max_length=10)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_s_products', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='S_Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondhands.s_product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='S_Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_purchases', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondhands.s_product')),
            ],
        ),
        migrations.CreateModel(
            name='S_ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=secondhands.models.S_ProductImage.s_product_image_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondhands.s_product')),
            ],
        ),
    ]
