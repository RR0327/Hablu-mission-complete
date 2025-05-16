from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CGPARecordViewSet, SkillViewSet, OutfitTipViewSet,
    MarathonEntryViewSet, GymFriendViewSet, MovieSuggestionViewSet,
    MoodCheckViewSet, JobViewSet, FunFactView, StudyGroupViewSet, HeroDashboardView
)

router = DefaultRouter()
router.register(r'cgpa', CGPARecordViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'outfit-tips', OutfitTipViewSet)
router.register(r'marathon', MarathonEntryViewSet)
router.register(r'gym-friends', GymFriendViewSet)
router.register(r'movies', MovieSuggestionViewSet)
router.register(r'mood-checks', MoodCheckViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'study-groups', StudyGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fun-fact/', FunFactView.as_view(), name='fun-fact'),  # ✅ Add this line
    path('dashboard/', HeroDashboardView.as_view(), name='hero-dashboard'),

]
