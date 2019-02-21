from django.urls import path, reverse_lazy

from roast.views import RoastCreate, RoastList

urlpatterns = [
    path('add', RoastCreate.as_view(success_url=reverse_lazy('index:home')), name="create"),
    path('roasts', RoastList.as_view(), name="list")
]