from django.contrib import admin
from django.urls import path, include
from app1 import urls as v1
from app2 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include(v1)), # 변경（app1의URL을 추가）
    path('app2/', v2.HomeView.as_view(), name="app2home"),
]
