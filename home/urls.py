from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:question_id>/savol/', Menu, name="savol"),
    # path('<int:question_id>/javoblar/', Vote, name="vote")
    # path('<int:question_id>/vote/', Ovozlar)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)