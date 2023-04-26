# файл с путями сайта
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import views_posts
urlpatterns = [
    path("", views.start, name='start'),
    path("chat-list/", views.index, name = 'index'),
    path("chat/<str:Id>/", views.chat, name='chat'),
    path("create-chat/", views.create_chat, name = "create-chat"),
    path("delete-chat/<str:Id>/", views.del_chat, name="delete-chat"),
    path("fix-chat/<str:Id>/", views.fix_chat, name="fix-chat"),
    path("del-message/<str:Id>/<str:id>/", views.del_message, name="del-message"),
    path("chat-up/<str:Id>/", views.chat_up, name="chat-up"),
    path("log-in/", views.log_user, name='log-user'),
    path("reg/", views.reg_user, name='reg-user'),
    path("log-out/", views.log_out, name='log-out'),
    path('change-password/', views.password_change , name='change-password'),

    path("post-list/", views_posts.posts, name='posts'),
    #path("del-comment/<str:Id>/<str:id>/", views_posts.del_comment, name="del-comment"),
    path("post-up/<str:Id>/", views_posts.post_up, name="post-up"),
    #path("post-comments/<str:Id>/", views_posts.post, name='post-comments'),
    path("create-post/", views_posts.create_post, name="create-post"),
    path("delete-post/<str:Id>/", views_posts.del_post, name="delete-post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


