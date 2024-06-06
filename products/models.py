from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CatalogModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'


class ManufacturerModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class ColorModel(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class TagModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class SizeModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class ProductsModel(models.Model):
    image1 = models.ImageField(upload_to='product-images')
    image2 = models.ImageField(upload_to='product-images', null=True)

    name = models.CharField(max_length=255)
    description = models.TextField()
    long_detail_description = models.TextField(null=True)
    count = models.IntegerField()
    sku = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    real_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    catalogs = models.ManyToManyField(CatalogModel, related_name='products')
    tags = models.ManyToManyField(TagModel, related_name='products')
    color = models.ManyToManyField(ColorModel, related_name='products')
    size = models.ManyToManyField(SizeModel, related_name='products')
    manufacturer = models.ForeignKey(ManufacturerModel, related_name='products', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def is_available(self):
        return self.count != 0

    def is_discounted(self):
        return self.discount != 0

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImagesModel(models.Model):
    image = models.ImageField(upload_to='product-detail-images')
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return self.product.name

    def __str__(self):
        return self.product.name


UserModel = get_user_model()
class ProductCommentsModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

