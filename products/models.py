from django.db.models import (
    DateTimeField, Model, CharField, SlugField,
    CASCADE, TextField, FloatField, ForeignKey,
    ImageField, PositiveIntegerField, TextChoices
)
from django.utils.timezone import now
from datetime import timedelta
from django.utils.text import slugify


class BaseCreatedModel(Model):
    updated_at = DateTimeField(auto_now_add=True, db_default=now())
    created_at = DateTimeField(auto_now=True, db_default=now())

    class Meta:
        abstract = True


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(
        self,
        raw=False,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        count = 0
        self.slug = slugify(self.name)

        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += f"_{count}"
            count += 1

        super().save(force_insert, force_update, using, update_fields)


class Category(BaseSlugModel):
    def __str__(self):
        return self.name


class Product(BaseSlugModel, BaseCreatedModel):
    description = TextField()
    price = FloatField()
    category = ForeignKey('products.Category', CASCADE, related_name='products')
    discount = PositiveIntegerField(default=0)
    quantity = PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Mahsulot'  # noqa
        verbose_name_plural = 'Mahsulotlar'  # noqa

    @property
    def is_new(self):
        return now() - self.created_at <= timedelta(days=7)

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(upload_to='products')
    product = ForeignKey('products.Product', CASCADE, related_name='images')

    def __str__(self):
        return f"image of {self.product.name}"

    class Meta:
        verbose_name = 'Mahsulot Rasmi'  # noqa
        verbose_name_plural = 'Mahsulot rasmlari'  # noqa


class Order(BaseCreatedModel):
    class OrderStatus(TextChoices):
        NEW = 'new', 'New'
        PENDING = 'pending', 'Pending'
        DELIVERED = 'delivered', 'Delivered'
        DONE = 'done', 'Done'

    product = ForeignKey('products.Product', CASCADE, 'orders')
    user = ForeignKey('users.User', CASCADE, 'orders')
    quantity = PositiveIntegerField()
    status = CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.NEW)

    def __str__(self):
        return f'user: {self.user.username} , {self.product.name} dan: {self.quantity} ta'

    class Meta:
        verbose_name = 'Buyurtma'  # noqa
        verbose_name_plural = 'Buyurtmalar'  # noqa


class Basket(Model):
    product = ForeignKey('products.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE, 'basket')
    quantity = PositiveIntegerField()

    def __str__(self):
        return self.product.name
