from django.shortcuts import render,HttpResponse,redirect
from app1.forms import MySiteUserForm,UserRoleForm,UserImageForm
from app1.models import MySiteUser,UserRole,UserImage
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
def index(request):
          return HttpResponse("<h1>Welcome to first response</h1>")
def home(request):
    return render(request,"home.html")
def about(request):
    name="Upasna"
    names=["upasna","sheikha","tanu"]
    return render(request,"about.html",{'n':name,'l':names})   #dict bnaege taki about m name dikhe
    #l key aur names dict m collections jara h

def testhome(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        form=MySiteUserForm(request.POST)
        f=form.save(commit=False)
        try:
            if request.FILES["userimage"]:
                my_file=request.FILES["userimage"]
                fs=FileSystemStorage()
                file_name=fs.save(my_file.name,my_file)
                userimage=fs.url(file_name)
                user_image=my_file.name
        except:
            pass
        f.userFullName=request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userPassword = request.POST["userpassword"]
        f.userMobile = request.POST["usermobile"]
        f.userImage = user_image
        f.isActive = True
        f.roleId_id=2
        f.save()
        return render(request,"signup.html",{'success':True})

    return render(request, "signup.html")


def userrole(request):
    if request.method=="POST":
        form=UserRoleForm(request.POST)
        f=form.save(commit=False)
        f.roleName= request.POST["t1"]
        f.isActive = True
        f.save()
        return render(request, "userrole.html", {'success': True})

    return render(request, "userrole.html")

def datafetch(request):
    data=MySiteUser.objects.all()
    #data=MySiteUser.objects.filter(isActive=1)
    #data=MySiteUser.objects.get(userEmail="up@gmail.com")
    return render(request,"viewdata.html",{'d':data})


def userimage(request):
    if request.method=="POST":
        form=UserImageForm(request.POST)
        f=form.save(commit=False)
        try:
            if request.FILES["userimage"]:           #agr user img upload kra h id dia
                my_file=request.FILES["userimage"]
                fs=FileSystemStorage()      #file sys storage ka obj
                file_name=fs.save(my_file.name,my_file)
                userimage=fs.url(file_name)      #instance passed in url
                user_image=my_file.name
        except:
            pass
        f.userFullName=request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userPassword =make_password(request.POST["userpassword"])
        f.userMobile = request.POST["usermobile"]
        #user_image=request.POST["userimage"]
        f.image=user_image
        f.isActive = True
        f.roleId_id=2
        f.save()
        return render(request,"img.html",{'success':True})

    return render(request, "img.html")


def update(request):
    if request.method=="POST":
        emailid=request.POST["useremail"]
        npassword=request.POST["userpassword"]
        mobile=request.POST["usermobile"]
        updatedata=UserImage(userEmail=emailid,userPassword=npassword,userMobile=mobile)
        updatedata.save(update_fields=["userPassword","userMobile"])

        #f.userFullName=request.POST["username"]
        #f.userEmail = request.POST["useremail"]
        #f.userPassword =make_password(request.POST["userpassword"])
        #f.userMobile = request.POST["usermobile"]
        #user_image=request.POST["userimage"]
        #f.image=user_image
        #f.isActive = True
        #f.roleId_id=2
        updatedata.save(update_fields=["userPassword","userMobile"])
        return render(request,"update.html",{'success':True})

    return render(request, "update.html")


def deletedata(request):
    emailId=request.GET["id"]
    data=MySiteUser.objects.get(userEmail=emailId)
    data.delete()
    return redirect("/viewdata/")


def datafetchup(request):
    emailId = request.GET["id"]
    data=MySiteUser.objects.get(userEmail=emailId)
    if request.method=="POST":
        name = request.POST["username"]
        password = request.POST["userpassword"]
        mobile = request.POST["usermobile"]
        updatedata = MySiteUser(userEmail=emailId, userPassword=password, userMobile=mobile,userFullName=name)
        updatedata.save(update_fields=["userPassword", "userMobile","userFullName"])
        return redirect("/viewdata/")
    return render(request,"edit.html",{'i':data})

def imgdetfetch(request):
    data = UserImage.objects.all()
    return render(request, "fetchimg.html", {'d': data})

def imagefetch(request):
    emailId = request.GET["id"]
    data=UserImage.objects.get(userEmail=emailId)
    if request.method=="POST":
        name=request.POST["username"]
        password=request.POST["userpassword"]
        mobile=request.POST["usermobile"]
        try:
            if request.FILES["userimage"]:
                my_file=request.FILES["userimage"]
                fs=FileSystemStorage()
                file_name=fs.save(my_file.name,my_file)
                userimage=fs.url(file_name)
                userimage=my_file.name
        except:
            pass
        updatedata = UserImage(userEmail=emailId,userPassword=password,userMobile=mobile,userFullName=name,image=userimage)
        updatedata.save(update_fields=["userPassword","userPassword","userMobile","userFullName","image"])
        return redirect("/fetchimg/")
    return render (request,"imgdatafetch.html",{'i':data})