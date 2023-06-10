# Generated by Django 3.2.18 on 2023-06-10 17:07

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import stores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('category', models.CharField(choices=[('미용', '미용'), ('의류', '의류'), ('잡화', '잡화'), ('기타', '기타')], max_length=10)),
                ('detail_image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.Product.p_product_image_path)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.Store.store_image_path)),
                ('main_image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.Store.store_image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('image1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductReview.product_review_image_path)),
                ('image2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductReview.product_review_image_path)),
                ('image3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductReview.product_review_image_path)),
                ('image4', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductReview.product_review_image_path)),
                ('image5', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductReview.product_review_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dislike_users', models.ManyToManyField(related_name='dislike_p_reviews', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_p_reviews', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_reviews', to='stores.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=stores.models.ProductImage.product_image_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stores.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.store'),
        ),
    ]
