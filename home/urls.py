from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:question_id>/savol/', Menu, name="savol"),
    # path('<int:question_id>/javoblar/', Vote, name="vote")
    # path('<int:question_id>/vote/', Ovozlar)
    path('add/question/', add_question, name='add_question')
]