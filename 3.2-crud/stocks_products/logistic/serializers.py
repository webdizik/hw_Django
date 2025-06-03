from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'price', 'quantity']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(stock=stock,  product=position['product'], defaults={'price': position['price'], 'quantity': position['quantity']})

        return stock


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


# class StockProductSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()

#     class Meta:
#         model = StockProduct
#         fields = ['product', 'price', 'quantity']

#         def create(self, validated_data):
#             product_data = validated_data.pop('product')
#             product, _ = Product.objects.get_or_create(title=product_data['title'], defaults={'description': product_data.get('description')})
#             stock_product = StockProduct.objects.create(product=product, **validated_data)

#             return stock_product

#         def update(self, instance, validated_data):
#             product_data = validated_data.pop('product', None)
#             if product_data:
#                 product, _ = Product.objects.get_or_create(title=product_data['title'], defaults={'description': product_data.get('description')})
#                 instance.product = product
#                 instance.price = validated_data.get('price', instance.price)
#                 instance.quantity = validated_data.get('quantity', instance.quantity)
#                 instance.save()

#                 return instance


#     class StockSerializer(serializers.ModelSerializer):
#         positions = StockProductSerializer(many=True)

#         class Meta:
#             model = Stock
#             fields = ['id', 'address', 'positions']

#             def create(self, validated_data):
#                 positions_data = validated_data.pop('positions')

#                 stock = super().create(validated_data)

#                 for position_data in positions_data:
#                     StockProductSerializer(data={**position_data, 'stock': stock}).save()

#                     return stock

#             def update(self, instance, validated_data):
#                 positions_data = validated_data.pop('positions', [])

#                 instance = super().update(instance, validated_data)

#                 instance.positions.all().delete()

#                 for position_data in positions_data:
#                     StockProductSerializer(data={**position_data, 'stock': instance}).save()

#                 return instance