from django.db import models
from django.urls import reverse
from account.models import TimeModel, User
from ckeditor.fields import RichTextField


class Article(TimeModel):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, related_name="articles", on_delete= models.CASCADE, null=True)
    body = RichTextField()
    slug = models.SlugField(null=True)
    likes = models.ManyToManyField(User, related_name="likes", null=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", null=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('article_detail', kwargs={'slug': self.slug})

    @property
    def number_of_comments(self):
        return Comment.objects.filter(article=self).count()

    @property
    def number_of_likes(self):
        return self.likes.count()

    @property
    def number_of_dislikes(self):
        return self.dislikes.count()

    @property
    def all_liked(self):
        return self.likes.all()

    @property
    def all_disliked(self):
        return self.dislikes.all()


class Comment(TimeModel):
    author = models.ForeignKey(User, related_name="comments", on_delete= models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", on_delete= models.CASCADE)
    body = models.TextField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.author) + ', ' + self.article.title[:40]