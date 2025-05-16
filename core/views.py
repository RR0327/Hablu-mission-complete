from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CGPARecord, Skill, OutfitTip, MarathonEntry, GymFriend, MovieSuggestion, MoodCheck, Job, StudyGroup
from .serializers import CGPARecordSerializer, SkillSerializer, OutfitTipSerializer, MarathonEntrySerializer, GymFriendSerializer, MovieSuggestionSerializer, MoodCheckSerializer, JobSerializer, StudyGroupSerializer
import random
from rest_framework.views import APIView
from rest_framework.response import Response

class CGPARecordViewSet(viewsets.ModelViewSet):
    queryset = CGPARecord.objects.all()
    serializer_class = CGPARecordSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class OutfitTipViewSet(viewsets.ModelViewSet):
    queryset = OutfitTip.objects.all()
    serializer_class = OutfitTipSerializer

class MarathonEntryViewSet(viewsets.ModelViewSet):
    queryset = MarathonEntry.objects.all()
    serializer_class = MarathonEntrySerializer

class GymFriendViewSet(viewsets.ModelViewSet):
    queryset = GymFriend.objects.all()
    serializer_class = GymFriendSerializer

class MovieSuggestionViewSet(viewsets.ModelViewSet):
    queryset = MovieSuggestion.objects.all()
    serializer_class = MovieSuggestionSerializer

class MoodCheckViewSet(viewsets.ModelViewSet):
    queryset = MoodCheck.objects.all()
    serializer_class = MoodCheckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_on')
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]  # only show to logged in users

class FunFactView(APIView):
    def get(self, request):
        facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
            "Bananas are berries, but strawberries aren't.",
            "Octopuses have three hearts and blue blood.",
            "A single sneeze travels 100 miles per hour and shoots 100,000 germs into the air.",
            "A day on Venus is longer than a year on Venus.",
            "Your heart beats about 100,000 times a day.",
            "Sharks existed before trees.",
            "Wombat poop is cube-shaped.",
            "The Eiffel Tower can be 15 cm taller during the summer.",
            "There are more stars in the universe than grains of sand on Earth."
        ]

        random_fact = random.choice(facts)
        return Response({"fun_fact": random_fact})
    
class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('scheduled_date', 'scheduled_time')
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class HeroDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        cgpa_count = CGPARecord.objects.filter(user=user).count()
        skill_count = Skill.objects.filter(user=user).count()
        mood_count = MoodCheck.objects.filter(user=user).count()
        marathon_count = MarathonEntry.objects.filter(user=user).count()
        group_joined_count = StudyGroup.objects.filter(members=user).count()

        total_jobs = Job.objects.all().count()  # global count
        outfit_tips = OutfitTip.objects.all().count()

        return Response({
            "user": user.username,
            "cgpa_records": cgpa_count,
            "skills_learned": skill_count,
            "mood_check_ins": mood_count,
            "marathon_sessions": marathon_count,
            "study_groups_joined": group_joined_count,
            "available_jobs": total_jobs,
            "outfit_tips_available": outfit_tips
        })