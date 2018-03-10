from rest_framework.serializers import ModelSerializer,CharField
from xshow.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
class UserSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=["UserId","Password"]
		
class UserLoginSerializer(ModelSerializer):
	token=CharField(label="Token",allow_blank="True",read_only="True")
	UserId=CharField(label="User Id")
	Password=CharField(label="Password")
	class Meta:
		model=User
		fields=["UserId","Password","token"]
		extra_kwargs={"Password":{"write_only":True}}
		
	def validate(self,data):
		userid=data.get("UserId")
		password=data.get("Password")
		
		user = User.objects.filter(Q(UserId=userid) & Q(Password=password))
		
		if user.exists()==False:
			data['token']=False
			raise ValidationError("user not found")
		else:
			data['token']=True
		return data