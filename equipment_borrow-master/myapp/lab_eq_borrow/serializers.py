from rest_framework import serializers
from .models import *

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultie
        fields = ('f_id','f_name')

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id','item_id_type','item_name','item_category',
                  'item_description','item_faculty','item_department',
                  'item_status','item_created_at','item_updated_at')
        
class UserPrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_privilege
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Id_type
        fields = '__all__'


class ItemCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_categorie
        fields = '__all__'


class ItemStatuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_statuse
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #
        extra_kwargs = {
            'password': {'write_only': True}
        }

    '''def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance'''
    #

class BorrowInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_info
        fields = '__all__'