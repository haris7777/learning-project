from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user_profile']


class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'profiles', 'id']

    # def get_prof(self, obj):
    #     qs = obj.prof.all()
    #     return ProfileSerializer(qs, many=True, read_only=True).data

    def create(self, validated_data):
        profs_data = validated_data.pop('profiles')
        user = User.objects.create(**validated_data)
        for prof_data in profs_data:
            Profile.objects.create(user=user, **prof_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        profiles = validated_data.get('profiles')
        profiles_dict = dict((i.id, i) for i in instance.profiles.all())


        for profile in profiles:
            profile_id = profile.get('id', None)

            if profile_id:
                multi_profile = Profile.objects.get(id=profile_id, user=instance)
                multi_profile.user_profile = profile.get('user_profile', multi_profile.user_profile)
                multi_profile.save()
            else:
                Profile.objects.create(user=instance, **profile)
        print(profiles_dict)
        if len(profiles_dict) > 0:
            for pro in profiles_dict.values():
                pro.delete()

        return instance






    # def update(self, instance, validated_data):
    #     profs_data = validated_data.pop('prof')
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.save()
    #     keep_profs_data = []
    #     # existing_ids = [c.id for c in instance.prof]
    #
    #     for prof_data in profs_data:
    #         if 'id' in profs_data.keys():
    #             if Profile.object.filter(id=prof_data[id].exist()):
    #                 c.user_profile = Profile.object.get('user_profile', c.user_profile)
    #                 c.save()
    #             else:
    #                 continue
    #         else:
    #             c = prof_data.object.create(**prof_data, user=instance)
    #             keep_profs_data.append(c.id)
    #     for prof_data in instance.profs_data:
    #         if prof_data.id not in keep_profs_data:
    #             prof_data.delete()
    #     return instance


    # def update(self, instance, validated_data):
    #     user_name = validated_data.pop('username')
    #     user_id = instance.id
    #     profile, updated = Profile.objects.update_or_create(user=instance, user_profile="oracle db")
    #
    #     return instance