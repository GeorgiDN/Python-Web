from furryFunniesApp.accounts.models import Author
from furryFunniesApp.posts.models import Post


def get_profile():
    return Author.objects.first()


def get_posts():
    return Post.objects.all()
