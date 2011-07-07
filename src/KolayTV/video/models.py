from django.db import models
import datetime
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length =50)
    caption = models.CharField(max_length = 250)
    tags = models.CharField(max_length = 30)
    video = models.FileField(upload_to="videos")
    slug = models.SlugField(unique_for_date = "pub_date")
    publisher = models.ForeignKey(User)
    pub_date = models.DateTimeField(default = datetime.datetime.now)
    featured = models.BooleanField(default = False)
    like = models.BooleanField(default = False)
    comments= models.CharField(max_length = 1000)
    class Meta:
        ordering =['-pub_date']
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/videos/%s/%s/%s" (self.User,self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    
    def  save(self,force_insert=False, force_update=False):
        super(Video, self).save(force_insert,force_update)
        