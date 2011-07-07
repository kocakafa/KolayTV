from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from KolayTV.video.models import Video
class Profile(models.Model):
        user = models.OneToOneField(User, verbose_name='Kullanıcı adı',
                                unique=True, db_index=True, editable=False)
        description = models.TextField(help_text="Genel bilgi",blank=True,null=True)
        profile_picture = models.ImageField(help_text="Kullanıcı fotoğrafı",upload_to="user_photo/" ,blank=True, null=True)
        url = models.URLField('Web sitesi', blank=True, null=True)
        def __unicode__(self):
            return '%s %s' % (self.user.first_name, self.user.last_name)
    
        @models.permalink
        def get_absolute_url(self):
            return ('profile_detail', (),
                    {'username' : self.user.username})

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)

        
        
