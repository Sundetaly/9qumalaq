from rest_framework import serializers

from core.constants import lang_kz, lang_en


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')

    def to_representation(self, instance):
        request = self.context.get('request')
        lang = request.query_params.get('lang')

        if lang == lang_kz:
            instance.name = instance.name_kz
        elif lang == lang_en:
            instance.name = instance.name_en
        
        return super(NameSerializer, self).to_representation(instance)


class LeaderShipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'rank', 'address', 'degree',
                  'description', 'bitrhday', 'assigned_degree')

    def to_representation(self, instance):
        request = self.context.get('request')
        lang = request.query_params.get('lang')

        if lang == lang_kz:
            instance.name = instance.name_kz
            instance.rank = instance.rank_kz
            instance.address = instance.address_kz
            instance.degree = instance.degree_kz
            instance.description = instance.description_kz
        elif lang == lang_en:
            instance.name = instance.name_en
            instance.rank = instance.rank_en
            instance.address = instance.address_en
            instance.degree = instance.degree_en
            instance.description = instance.description_en
            
        return super(LeaderShipSerializer, self).to_representation(instance)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'published', 'altered')

    def to_representation(self, instance):
        request = self.context.get('request')
        lang = request.query_params.get('lang')

        if lang == lang_kz:
            instance.title = instance.title_kz
            instance.description = instance.description_kz
        elif lang == lang_en:
            instance.title = instance.title_en
            instance.description = instance.description_en
            
        return super(NewsSerializer, self).to_representation(instance)
