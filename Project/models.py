from django.db import models

# Create your models here.

class Area(models.Model):
    pincode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zone = models.CharField(max_length=25)
    recorded_date = models.DateField(auto_now_add=True)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class ProjectIdentifier(models.Model):
    project = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class Platform(models.Model):
    platform_name = models.CharField(max_length=50)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_url = models.CharField(max_length=500)
    recorded_date = models.DateField()
    is_active = models.IntegerField()
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING, default=1)
    project_identifier = models.ForeignKey(ProjectIdentifier, on_delete=models.DO_NOTHING)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class ProductArea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class PlatformArea(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    project_identifier = models.ForeignKey(ProjectIdentifier, on_delete=models.DO_NOTHING)
    recorded_date = models.DateField()
    is_active = models.IntegerField()


class ProductDetails(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    crawl_date = models.DateField()
    product_weight = models.CharField(max_length=50, null=True)
    bestseller_rank = models.CharField(max_length=50, null=True, blank=True)
    seller_name = models.CharField(max_length=250)
    main_seller = models.CharField(max_length=3)
    price = models.FloatField()
    promo = models.CharField(max_length=5)
    availability = models.IntegerField()
    overall_rating = models.CharField(max_length=10, null=True)
    total_ratings = models.CharField(max_length=10, null=True)
    five_stars_rating = models.CharField(max_length=10, null=True)
    four_stars_rating = models.CharField(max_length=10, null=True)
    three_stars_rating = models.CharField(max_length=10, null=True)
    two_stars_rating = models.CharField(max_length=10, null=True)
    one_star_rating = models.CharField(max_length=10, null=True)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class KeywordTbl(models.Model):
    keyword = models.CharField(max_length=100)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class KeywordTblArea(models.Model):
    keyword = models.ForeignKey(KeywordTbl, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    project_identifier = models.ForeignKey(ProjectIdentifier, on_delete=models.DO_NOTHING)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING, default=1)
    recorded_date = models.DateField()
    is_active = models.IntegerField()
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class KeywordSearchResult(models.Model):
    keyword = models.ForeignKey(KeywordTbl, on_delete=models.DO_NOTHING)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    search_category = models.IntegerField()
    product_name = models.CharField(max_length=250)
    product_rank = models.IntegerField()
    crawl_date = models.DateField()
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class BestsellerCategory(models.Model):
    category_name = models.CharField(max_length=50)
    recorded_date = models.DateField()
    is_active = models.IntegerField()
    category_url = models.CharField(max_length=500, default=None, null=True)
    project_identifier = models.ForeignKey(ProjectIdentifier, on_delete=models.DO_NOTHING)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class AmazonBestsellerRank(models.Model):
    crawl_date = models.DateField()
    bestseller_category = models.ForeignKey(BestsellerCategory, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=500)
    product_rank = models.IntegerField()
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    crawl_date = models.DateField()
    review_id = models.CharField(max_length=15, null=True, blank=True)
    review_date = models.DateField(null=True, blank=True)
    review_title = models.CharField(max_length=250, blank=True, null=True)
    review_body = models.TextField(blank=True)
    positive_score = models.FloatField()
    neutral_score = models.FloatField()
    negative_score = models.FloatField()
    compound_score = models.FloatField()
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)


class ReviewReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    crawl_date = models.DateField()
    reviews_count = models.IntegerField(null=True)
    aggregate_score = models.FloatField(null=True)
    meter_url = models.CharField(max_length=350, blank=True, null=True)
    positive_wordcloud_url = models.CharField(max_length=350, blank=True, null=True)
    negative_wordcloud_url = models.CharField(max_length=350, blank=True, null=True)
    extra_field1 = models.CharField(max_length=100, null=True, blank=True)
    extra_field2 = models.CharField(max_length=100, null=True, blank=True)
    extra_field3 = models.CharField(max_length=100, null=True, blank=True)
    extra_field4 = models.CharField(max_length=100, null=True, blank=True)
    extra_field5 = models.CharField(max_length=100, null=True, blank=True)