from django.contrib import admin 
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings # new
from  django.conf.urls.static import static #new


# router = DefaultRouter()

# router.register('Book', views.BookViewSet, basename='Book')
# router.register('Chapter', views.ChapterViewSet, basename='Chapter')
# router.register('Subhead1', views.Subhead1ViewSet, basename='Subhead1')


admin.site.site_header = 'SadlecBooks Administration'
admin.site.site_title = 'SadlecBooks admin'
admin.site.index_title = 'SadlecBooks Admin Area'



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api/user/', include('account.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('api.urls')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   
    # path('book/<int:pk>/', views.bookdetail),
    # path('book/', views.booklist),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
