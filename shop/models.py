from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    desc = models.TextField(verbose_name='Category Description', null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category/', verbose_name='Category Image', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            counter = 2
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = '{}-{}'.format(base_slug, counter)
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# class Product(models.Model):
#     title = models.CharField(max_length=500)
#     slug = models.SlugField(unique=True, blank=True)
#     sku = models.CharField(max_length=10)
#     org_price = models.IntegerField(verbose_name='Original Price or Old Price')
#     price = models.IntegerField(verbose_name='Discounted Price or New Price')
#     short_desc = models.TextField(verbose_name='Short Description')
#     image = models.ImageField(upload_to='/product', verbose_name='Main Image or Featured Image')
#     best_selling = models.BooleanField(default=False, verbose_name='Is Best Selling Product')
#     featured = models.BooleanField(default=False, verbose_name='Is Featured Product')
#     today_sell =models.BooleanField(default=False, verbose_name='Is Product for Today Sell')


#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.title)
#             self.slug = base_slug
#             counter = 2
#             while Product.objects.filter(slug=self.slug).exists():
#                 self.slug = '{}-{}'.format(base_slug, counter)
#                 counter += 1
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title