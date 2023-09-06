# Generated by Django 4.2.5 on 2023-09-05 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('pincode', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zone', models.CharField(max_length=25)),
                ('recorded_date', models.DateField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_url', models.CharField(max_length=500)),
                ('recorded_date', models.DateField()),
                ('is_active', models.IntegerField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('platform', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawl_date', models.DateField()),
                ('reviews_count', models.IntegerField(null=True)),
                ('aggregate_score', models.FloatField(null=True)),
                ('meter_url', models.CharField(blank=True, max_length=350, null=True)),
                ('positive_wordcloud_url', models.CharField(blank=True, max_length=350, null=True)),
                ('negative_wordcloud_url', models.CharField(blank=True, max_length=350, null=True)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawl_date', models.DateField()),
                ('review_id', models.CharField(blank=True, max_length=15, null=True)),
                ('review_date', models.DateField(blank=True, null=True)),
                ('review_title', models.CharField(blank=True, max_length=250, null=True)),
                ('review_body', models.TextField(blank=True)),
                ('positive_score', models.FloatField()),
                ('neutral_score', models.FloatField()),
                ('negative_score', models.FloatField()),
                ('compound_score', models.FloatField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawl_date', models.DateField()),
                ('product_weight', models.CharField(max_length=50, null=True)),
                ('bestseller_rank', models.CharField(blank=True, max_length=50, null=True)),
                ('seller_name', models.CharField(max_length=250)),
                ('main_seller', models.CharField(max_length=3)),
                ('price', models.FloatField()),
                ('promo', models.CharField(max_length=5)),
                ('availability', models.IntegerField()),
                ('overall_rating', models.CharField(max_length=10, null=True)),
                ('total_ratings', models.CharField(max_length=10, null=True)),
                ('five_stars_rating', models.CharField(max_length=10, null=True)),
                ('four_stars_rating', models.CharField(max_length=10, null=True)),
                ('three_stars_rating', models.CharField(max_length=10, null=True)),
                ('two_stars_rating', models.CharField(max_length=10, null=True)),
                ('one_star_rating', models.CharField(max_length=10, null=True)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='project_identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.projectidentifier'),
        ),
        migrations.CreateModel(
            name='PlatformArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_date', models.DateField()),
                ('is_active', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
                ('project_identifier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.projectidentifier')),
            ],
        ),
        migrations.CreateModel(
            name='KeywordTblArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_date', models.DateField()),
                ('is_active', models.IntegerField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.keywordtbl')),
                ('platform', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
                ('project_identifier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.projectidentifier')),
            ],
        ),
        migrations.CreateModel(
            name='KeywordSearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_category', models.IntegerField()),
                ('product_name', models.CharField(max_length=250)),
                ('product_rank', models.IntegerField()),
                ('crawl_date', models.DateField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.keywordtbl')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.platform')),
            ],
        ),
        migrations.CreateModel(
            name='BestsellerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('recorded_date', models.DateField()),
                ('is_active', models.IntegerField()),
                ('category_url', models.CharField(default=None, max_length=500, null=True)),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('project_identifier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.projectidentifier')),
            ],
        ),
        migrations.CreateModel(
            name='AmazonBestsellerRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawl_date', models.DateField()),
                ('product_name', models.CharField(max_length=500)),
                ('product_rank', models.IntegerField()),
                ('extra_field1', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field2', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field3', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field4', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_field5', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.area')),
                ('bestseller_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.bestsellercategory')),
            ],
        ),
    ]
