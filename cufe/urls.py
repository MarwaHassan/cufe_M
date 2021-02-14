"""cufe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import view_user_items, get_category_models, get_proc_entities, \
    view_item_entries, view_item_entries2, DynamicUpdateView, DynamicCreateView, \
    contactus, approve_entry, Dash_CHS, Dash_SCI, Dash_STUD, JSON_test, send_item_Notification
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('fold/', include('forms.urls')),
    path('get_models/<int:categ_id>', get_category_models),
    path('get_proc_ent/<int:ent_type_id>', get_proc_entities),
    path('approventry/<int:item_id>/-<int:entry_id>', approve_entry),
    path('itementries2/<int:item_id>', view_item_entries2),
    path('itementries/<int:item_id>', view_item_entries),
    # path('itemform/', view_item_form),
    # path('itemedit/<int:pk>', DynamicView.as_view()),
    path('itemedit/<int:item_id>/<int:pk>', DynamicUpdateView.as_view(), name='update-item'),
    path('itemadd/<int:item_id>', DynamicCreateView.as_view(), name='create-item'),
    path('sendNotifications/<int:item_id>', send_item_Notification),
    path('itemaddnext/<int:item_id>', DynamicCreateView.as_view(), name='create-next-item'),
    path('', view_user_items, name='list-items'),
    path('contactus/',contactus, name='contactus'),
    path('Dash_CHS/',Dash_CHS, name='Dash_CHS'),
    path('Dash_SCI/',Dash_SCI, name='Dash_SCI'),
    path('Dash_STUD/',Dash_STUD, name='Dash_STUD'),
    path('jsontest/', JSON_test, name='JSON_test'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

