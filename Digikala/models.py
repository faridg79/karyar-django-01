from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Seller(models.Model):
    CHOICES_PERFORMANCE = (
        ('Poor', 'Poor'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=150)
    seller_performance = models.CharField(choices=CHOICES_PERFORMANCE)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.seller_name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    postal_code = models.PositiveIntegerField()
    phone = models.PositiveIntegerField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    national_code = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    CHOICES_ORGINAL = (
        (True, 'Yes'),
        (False, 'No')
    )

    title = models.CharField(max_length=250, unique=True)
    thumbnail = models.ImageField(upload_to="product_pics/")
    colors = models.CharField(max_length=150, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    product_introduction = models.TextField()
    review_product = models.TextField()
    product_specifications = models.TextField()
    product_inventory = models.PositiveIntegerField()
    orginal = models.BooleanField(choices=CHOICES_ORGINAL)
    price = models.PositiveIntegerField()
    sellers = models.ManyToManyField(Seller)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


class Order(models.Model):
    CHOICES_STATUS = (
        ('Canceled', 'Canceled'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned')
    )
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_code = models.PositiveIntegerField(unique=True)
    order_status = models.CharField(max_length=150, choices=CHOICES_STATUS)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
