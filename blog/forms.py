from django.forms import ModelForm
from blog.models import BlogPostModel


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPostModel
        fields = '__all__'


