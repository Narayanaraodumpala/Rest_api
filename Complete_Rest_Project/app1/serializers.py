from rest_framework import serializers
from .models import *
class carspaxceserializers(serializers.ModelSerializer):
    class Meta:
        model=CarspaceModel
        fields=('car_number','car_plan','car_tyres','car_name','car_brand','description','production','fuel')
        depth = 1


class Tyreserializers(serializers.ModelSerializer):
      class Meta:
          model=TyreModel
          fields="__all__"






class Carplanserializers(serializers.ModelSerializer):
    class Meta:
        model=Carplan
        fields=('car','plan_id','plan_name','current_status','plan_validity')




from allauth.account.adapter import get_adapter
from Complete_Rest_Project import settings
from .models import User
from allauth.account.utils import  setup_user_email

class RegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    first_name=serializers.CharField(required=False,write_only=True)
    last_name=serializers.CharField(required=False,write_only=True)
    address=serializers.CharField(required=False,write_only=True)

    password1=serializers.CharField(required=False,write_only=True)
    password2=serializers.CharField(required=False,write_only=True)

    def validate_password1(self,password):
        return get_adapter().clean_password(password)

    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(("the two password fields didn't matched.."))
        return data


    def get_cleaned_data(self):
        return {
            'first_name':self.validated_data.get('first_name', ''),
            'last_name':self.validated_data.get('last_name',''),
            'address':self.validated_data.get('address',''),
            'user_type':self.validated_data.get('user_type',''),
            'password1':self.validated_data.get('password1',''),
            'email':self.validated_data.get('email','')
        }
    def save(self, request):
        adapter=get_adapter()
        user=adapter.new_user(self,request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request , user,self)
        self.custom_signup(request,user)
        setup_user_email(request,user,[])
        return user

        user.save()
        return User


class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('pk','username','email','first_name','last_name',
                'address',
                'city','about_me','profile_image')

        read_only_fields=('email', )

