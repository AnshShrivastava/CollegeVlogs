from django.db import models
import uuid


class College(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    video = models.URLField(null=False)
    description = models.TextField()
    banner = models.ImageField()
    location = models.TextField()
    
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
    
         
class Vlogs(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    college_id = models.ForeignKey('College', on_delete=models.CASCADE)
    vlogger_id = models.ForeignKey('Vlogger', on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    video = models.URLField()
    banner = models.ImageField()
    views = models.IntegerField()
    
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
        return (self.name + " " + self.college)
    
    