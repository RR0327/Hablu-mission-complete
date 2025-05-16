from rest_framework import serializers
from .models import CGPARecord, Skill, OutfitTip, MarathonEntry, GymFriend, MovieSuggestion, MoodCheck, Job, StudyGroup

class CGPARecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CGPARecord
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class OutfitTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitTip
        fields = '__all__'


class MarathonEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarathonEntry
        fields = '__all__'

class GymFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymFriend
        fields = '__all__'

class MovieSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSuggestion
        fields = '__all__'

class MoodCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodCheck
        fields = ['id', 'user', 'mood', 'note', 'date']
        read_only_fields = ['date']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'category', 'apply_link', 'posted_on']

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['id', 'topic', 'description', 'scheduled_date', 'scheduled_time', 'created_by', 'members']
        read_only_fields = ['created_by']
