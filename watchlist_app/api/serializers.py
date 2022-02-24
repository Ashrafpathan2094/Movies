
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Reviews

class ReviewsSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Reviews
        exclude = ('watchlist',)
        # fields = '__all__'
        
    


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True , read_only = True)
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist = WatchListSerializer(many =True , read_only = True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'









        # fields = ['id','name','description']
        # exclude = ['description']
        
        
        
    # def get_len_name(self,object): 
    #     return len(object.name)
        
  
            

# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Nmae too short")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active')
#         instance.save()
#         return instance
    
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Both Shouldnt be equal")
#         else:
#             return data
            
    
 