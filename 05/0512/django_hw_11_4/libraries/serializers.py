from rest_framework import serializers
from .models import Book, Review


class ReviewListSerializer(serializers.ModelSerializer):
    isbn = serializers.ReadOnlyField(source='book.isbn')
    class Meta:
        model = Review
        fields = ('content', 'score', 'isbn')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()
    review_list = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

    def get_review_count(self, obj):
        return obj.review_set.count()