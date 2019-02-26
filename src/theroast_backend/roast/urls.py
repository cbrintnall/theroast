from django.urls import path, reverse_lazy

from roast.views import *

urlpatterns = [
    path('add', RoastCreate.as_view(success_url=reverse_lazy('index:home')), name="create"),
    path('roasts', RoastList.as_view(), name="list"),
    path('/<int:pk>', RoastCreate.as_view(), name="list"),
    path('detail/<int:pk>', RoastCrud.as_view(), name="list"),
]