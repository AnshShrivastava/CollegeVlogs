from django.db import models
from embed_video.fields import EmbedVideoField
import uuid



class College(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    collegename = models.TextField(default="")
    video = models.URLField(null=False)
    description = models.TextField()
    banner = models.ImageField()
    location = models.TextField()

    def __str__(self):
        return self.collegename
    
class Vlogger(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    age = models.IntegerField()
    college = models.TextField()
    facebook = models.TextField()
    phone_mobile = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    channel = models.URLField()
    image = models.ImageField()
    bio = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name
    
         
class Vlogs(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    college_id = models.ForeignKey('College', on_delete=models.CASCADE)
    vlogger_id = models.ForeignKey('Vlogger', on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    # video = models.URLField()
    video = EmbedVideoField()
    banner = models.ImageField()
    views = models.IntegerField()

    def __str__(self):
        return self.vlogger_id.name + " - " + self.college_id.collegename
    
class Leads(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    college = models.TextField(null=True)
    name = models.TextField(null=True)
    email = models.EmailField(null=True)
    college_email = models.EmailField(null=True)
    request = models.TextField(null=True) 
    def __str__(self):
        return (self.name + " " + self.college)    
    
class Registrations(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    
    
    
class FAQs(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    college = models.TextField()
    college_location = models.TextField()
    name = models.TextField(null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    college_email = models.EmailField(null=True)
    message = models.TextField()
    
    
class Requests(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    college = models.TextField()
    name = models.TextField(null=True)
    email = models.EmailField(null=True)
    file = models.FileField(upload_to='data',default="Null")
    request = models.TextField()

    def __str__(self):
        return (self.name + " - " + self.college)