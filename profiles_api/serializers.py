from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing api view """

    name = serializers.CharField(max_length=10) 


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')

        # add custom properties to UserProfile model fields 
        extra_kwargs = {
            'password': {
                # only relevant in create / update model instance 
                'write_only': True, 

                # not displaying password field when being typed 
                'style': {
                    'input_type': 'password'
                }

            }
        }

    # first user data is validated, then passed to create a new user 
    def create(self, validated_data):
        """ Create and return a new user """

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )

        return user 




    