from rest_framework import serializers
from .models import Todo, Recommend


class TodoSerializer(serializers.ModelSerializer):
    class  RecommendSerialzerForTodoDetail(serializers.ModelSerializer):
        class Meta:
            model = Recommend
            fields = ('content',)
    recommend_set = RecommendSerialzerForTodoDetail(many=True, read_only=True)
    num_of_recommends = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields = '__all__'

    def get_num_of_recommends(self, obj):
        return obj.num_of_recommends


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
        read_only_fields = ('todo',)

