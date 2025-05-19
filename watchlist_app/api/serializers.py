from rest_framework import serializers

from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    # FIELD VALIDATION EXAMPLE
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be greater than 2 characters, because it's too short.")
        return value

    # OBJECT VALIDATION EXAMPLE
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description cannot be the same, please change one.")
        return data


# VALIDATOR EXAMPLE ALMOST SAME AS FIELD VALIDATION
# def name_length_validator(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short.")
#     return value
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length_validator])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # FIELD VALIDATION EXAMPLE
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name must be greater than 2 characters.")
    #     return value

    # OBJECT VALIDATION EXAMPLE
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description cannot be the same.")
    #     return data
















