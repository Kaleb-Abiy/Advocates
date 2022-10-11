from rest_framework import serializers
from . models import Company, Advocate, AdvocateLink


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'logo', 'summary']

class AdvocateLinkListSeriizer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateLink
        fields = ['youtube', 'github', 'twitter']

class AdvocateListSerializer(serializers.ModelSerializer):
    links = AdvocateLinkListSeriizer()
    class Meta:
        model = Advocate
        fields = ['id','name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'links']



class CompanySerializer(serializers.ModelSerializer):
    advocates = AdvocateListSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id','name', 'logo', 'summary', 'advocates']



    


class AdvocateLinkSeriizer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateLink
        fields = ['youtube', 'github', 'twitter']


class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanyListSerializer()
    links = AdvocateLinkSeriizer()
    class Meta:
        model = Advocate
        fields = ['id','name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'company', 'links']

    
    # def create(self, validated_data):
    #     company_data = validated_data['company']

    #     advocate = Advocate.objects.create(**validated_data)
    #     company = Company.objects.create(adv**company_data)


