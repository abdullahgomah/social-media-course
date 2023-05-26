from django.db import models
from django.utils.text import slugify

from author.models import Author

# Create your models here.



class Post(models.Model):
    POST_TYPE_CHOICES = (
        ('question', 'سؤال'),
        ('post', 'منشور'),
        ('article', 'مقالة'),
    )

    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True)

    # المستخدم صاحب المنشور
    p_type = models.CharField(max_length=60, choices=POST_TYPE_CHOICES, verbose_name="نوع المنشور")
    title=  models.CharField(max_length=200, verbose_name="عنوان المنشور")
    content = models.TextField(verbose_name="محتوى المنشور")
    likes = models.IntegerField(default=0, verbose_name="الإعجاب")
    dislikes = models.IntegerField(default=0, verbose_name="ديسلايك")
    date_published = models.DateTimeField(auto_now=False) # Schedule Posts
    
    categories = models.ManyToManyField("Category", verbose_name="الأقسام")

    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, allow_unicode=True)

    

    class Meta:
        verbose_name = "منشور"
        verbose_name_plural ="المنشورات"


    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):  
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs) 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="المنشور") 
    ## المستخدم صاحب التعليق
    content = models.TextField(verbose_name="التعليق")
    date_published = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = 'تعليق'
        verbose_name_plural = "التعليقات"

    def __str__(self):
        return self.content[:10]

class Category(models.Model):
    name= models.CharField(max_length=70) 

    def __str__(self): 
        return self.name
    
    class Meta:
        verbose_name = 'قسم '
        verbose_name_plural = 'الأقسام '