from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UsersViewSet, user_sign_up, obtain_pair,
    CategoryViewSet, GenreViewSet, ReviewViewSet,
    TitleViewSet, CommentViewSet
)

app_name = 'api'

router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
router.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments',
)

extra_patterns = [
    path(
        'token/',
        obtain_pair,
        name='token_obtain_pair'
    ),
    path(
        'signup/',
        user_sign_up,
        name='user_sign_up'
    ),
]
urlpatterns = [
    path(
        'v1/auth/',
        include(extra_patterns)
    ),

    path('v1/', include(router.urls)),
]