from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forumApp.posts'

    def ready(self):
        import forumApp.posts.signals
