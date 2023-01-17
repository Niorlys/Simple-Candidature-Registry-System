from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *

router = SimpleRouter()
router.register('candidates', CandidateView, basename='Cnadidates')
router.register('tech', TechView, basename='Technologies')
router.register('candidatetech', CandidateTechView, basename='Experience')

urlpatterns =  [path('report', Report.as_view())] + router.urls