from django.db import models
from django.contrib import messages

import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['fname']) < 2:
            errors["name"] = "First  name should be at least 2 characters !"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters !"
        EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="invalid email address!"
        if len(postData['pwd']) < 8:
            errors["pwd"] = "password should be at least 8 characters!"
        
    
        return errors


class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects =UserManager()
# Create your models here.
class Message(models.Model):
    message=models.TextField()
    user = models.ForeignKey(User, related_name='messages',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    comment=models.TextField()
    user = models.ForeignKey(User, related_name='comments',on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)