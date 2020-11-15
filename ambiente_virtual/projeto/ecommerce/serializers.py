from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Produto



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['produto_nome', 'produto_marca', 'produto_categoria', 'produto_valor', 'produto_estoque', 'produto_avaliacao', 'produto_garantia' ]
    
