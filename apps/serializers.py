from rest_framework import routers, serializers, viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from apps.models import User, Product, Order, OrderItem, ShippingAddress
# from apps.views import UserViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'sex', 'birth_date', 'is_staff']



# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)
#
#     # def create(self, request, *args, **kwargs):
#     #     name = request.data['username']
#     #     email = request.data['email']
#     #     password = request.data['password']
#     #     password2 = request.data['password2']
#     #     birth_date = request.data['birth_date']
#     #
#     #     if password == password2:
#     #         if User.objects.filter(email=email).exists():
#     #             return Response({'error': 'Email already exists'})
#     #         else:
#     #             if len(password) < 6:
#     #                 return Response({'error': 'Password must be at least 6 characters'})
#     #             else:
#     #                 user = User.objects.create_user(username=name, email=email, password=password,
#     #                                                 birth_date=birth_date)
#     #                 user.save()
#     #                 return Response({'success': 'User created successfully'})
#     #     else:
#     #         return Response({'error': 'Passwords do not match'})




# Routers provide a way of automatically determining the URL conf.


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # image = serializers.ImageField(max_length=None)

    class Meta:
        model = Product
        # fields = ['url','name', 'price', 'description', 'digital', 'image']
        fields = '__all__'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = (IsAuthenticated,)

    #
    def create(self, request, *args, **kwargs):
        name= request.data['name']
        price = request.data['price']
        description = request.data['description']
        digital = request.data['digital']
        image = request.data['image']

        Product.objects.create(name=name, price=price, description=description, digital=digital, image=image)
        return Response(status=status.HTTP_201_CREATED)




class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = (IsAuthenticated,)


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'orders', OrderViewSet)
# router.register(r'orderitems', OrderItemViewSet)
# router.register(r'shippingaddress', ShippingAddressViewSet)
