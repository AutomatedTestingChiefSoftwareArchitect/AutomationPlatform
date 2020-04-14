from django.conf.urls import url
from DjangoRESTFramework.RestFrameworkUser \
    import Interfacelogin, InterfaceProject, InterfacePlatform, InterfaceApi, DataPool

urlpatterns = [

    # 用户
    url(r'interfaceauth/$', Interfacelogin.AuthView.as_view()),

    url(r'interfaceproject/$', InterfaceProject.UserAllProject.as_view({'get': 'user_project',
                                                                        'post': 'create_project',
                                                                        'put': 'update_project',
                                                                        'delete': 'delete_project'})),

    url(r'interfaceplatform/$', InterfacePlatform.AutomatedPlatformView.as_view({'get': 'platforminterface',
                                                                                 'post': 'interfaceproject'})),

    url(r'interfaceapi/$', InterfaceApi.UserApiInfoView.as_view({'post': 'api_save',
                                                                 'put': 'update_api',
                                                                 'delete': 'delete_api'}))
]
