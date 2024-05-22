from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog-authors')
    about = models.TextField()
    position = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BlogTagModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog-images')
    content = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField(BlogTagModel, related_name='blogs')
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
