from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.apps import apps

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    SEX_CHOISE = [
        (1, 'Man'),
        (2,  'Woman')
    ]

    sex=models.PositiveIntegerField(verbose_name="sex", choices=SEX_CHOISE, blank=True, default=1)
    birth_date = models.DateField(verbose_name="birthday" , null=True, blank=True)



    email=models.EmailField(verbose_name="email", unique=True, error_messages={
            "unique": _("A user  with that email already exists."),
        },)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        validators=[username_validator],
        blank=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # objects = UserManager()







class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.TextField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order =  models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems =self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item  in orderitems])
        return total

    @property
    def shipping(self):
        shipping =False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False :
                shipping = True
        return  shipping


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price *self.quantity
        return total

    # def __str__(self):
    #     return f'{self.email, self.username, self.}'


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,  on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.address


