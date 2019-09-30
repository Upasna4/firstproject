from django import forms
from app1.models import MySiteUser,UserRole,UserImage


class MySiteUserForm(forms.ModelForm):
    class Meta():
        model=MySiteUser
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "userImage",
                 "isActive"
                 ]

class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        exclude=["roleId",
                 "roleName",
                 "isActive"
                 ]

class UserImageForm(forms.ModelForm):
    class Meta():
        model=UserImage
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "image",
                 "isActive"
                 ]
