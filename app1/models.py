from django.db import models

# Create your models here.
class UserRole(models.Model):
    roleId=models.AutoField(primary_key=True)
    roleName=models.CharField(max_length=200,default="")
    isActive=models.BooleanField(default=True)

class MySiteUser(models.Model):
    roleId=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    userFullName=models.CharField(max_length=200,default="")
    userEmail=models.CharField(primary_key=True,max_length=200,default="")
    userPassword=models.CharField(max_length=200,default="")
    userMobile=models.BigIntegerField()
    userImage = models.CharField(max_length=200, default="")
    isActive=models.BooleanField(default=True)

class UserImage(models.Model):
        roleId = models.ForeignKey(UserRole, on_delete=models.CASCADE)
        userFullName = models.CharField(max_length=200, default="")
        userEmail = models.CharField(primary_key=True, max_length=200, default="")
        userPassword = models.CharField(max_length=200, default="")
        userMobile = models.BigIntegerField()
        image = models.CharField(max_length=200, default="")
        isActive = models.BooleanField(default=True)



