from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,default=None,null=True,blank=True)
    last_name = models.CharField(max_length=50,default=None,null=True,blank=True)
    place = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    dob = models.DateField()
    picture = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_pics')
    # likes= models.IntegerField(default=0)
    # dislikes= models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts',blank=True )
    # dislikes = models.ManyToManyField(User, related_name='disliked_posts')

    def __str__(self):
        return self.title

# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'post')

