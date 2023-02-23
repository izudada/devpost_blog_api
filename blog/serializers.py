from rest_framework import serializers

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'body', 'slug', 'likes', 'dislikes', 'created_at']

        def save(self, user, slug):
            """
                A method overiding DRF serializer's save method
            """
            new_article = Article(
                title = self.validated_data.get("title"),
                author = user,
                body = self.validated_data.get("body"),
                slug = slug
            )
            new_article.save()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'article', 'body', 'created_at']

        def save(self, author, article):
            """
                A method overiding DRF serializer's save method
            """
            new_comment = Comment(
                author=author,
                article = article,
                body=self.validated_data.get("body")
            )
            new_comment.save()
