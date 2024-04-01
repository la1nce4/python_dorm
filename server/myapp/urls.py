from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    # api
    path('admin/overview/count', views.admin.overview.count),
    path('admin/overview/sysInfo', views.admin.overview.sysInfo),

    path('admin/thing/list', views.admin.thing.list_api),
    path('admin/thing/detail', views.admin.thing.detail),
    path('admin/thing/create', views.admin.thing.create),
    path('admin/thing/update', views.admin.thing.update),



    path('admin/user/list', views.admin.user.list_api),
    path('admin/user/create', views.admin.user.create),
    path('admin/user/update', views.admin.user.update),
    path('admin/user/updatePwd', views.admin.user.updatePwd),
    path('admin/user/delete', views.admin.user.delete),
    path('admin/user/info', views.admin.user.info),

    path('admin/adminLogin', views.admin.user.admin_login),

    path('admin/classification/create', views.admin.classification.create),
    path('admin/classification/list', views.admin.classification.list_api),

    path('admin/tag/list', views.admin.tag.list_api),

    path('admin/loginLog/list', views.admin.loginLog.list_api),

    path('admin/opLog/list', views.admin.opLog.list_api),

    path('admin/errorLog/list', views.admin.errorLog.list_api),



]
