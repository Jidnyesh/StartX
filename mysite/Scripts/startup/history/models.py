from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from history.signals import object_viewed_signal
from django.contrib.sessions.models import Session
#from history.utils import get_client_ip
#from django.db.models import pre_save , post_save
# Create your models here.
User = settings.AUTH_USER_MODEL
class ObjectView(models.Model):
    ip_add = models.CharField(max_length=120,blank=True,null=True)
    content_type    = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type','object_id')
    timeview = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.content_object

    class Meta:
        ordering = ['-timeview']


def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    print(instance)
    new_view_obj = ObjectView.objects.create(content_type=c_type,object_id=instance.id)

object_viewed_signal.connect(object_viewed_receiver)
