from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
]