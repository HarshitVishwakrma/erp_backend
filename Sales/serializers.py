from rest_framework import serializers
from .models import onwardchallan
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan
# from .views import generate_unique_challan_number

class OnwardChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = onwardchallan
        fields = '__all__'
class transportdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=transportdetails
        fields='__all__'
class vehicaldetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicaldetails
        fields='__all__'
class outwardchallanSerializer(serializers.ModelSerializer):
    class Meta:
        model=outwardchallan
        fields='__all__'
