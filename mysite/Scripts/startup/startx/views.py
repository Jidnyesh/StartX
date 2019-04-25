from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth import login , authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,AddProductForm,AuthenticationLoginForm,AddJobForm,CompleteProfileForm,UserEditForm,CommentForm,AddAdvertisementForm
from .models import Product,Job,Profile,Comments,Advertisement

from django.contrib.auth.models import Group
from django.db.models import Q
import urllib
from django.conf import settings
import json
from history.signals import object_viewed_signal
from history.models import ObjectView
from datetime import datetime,timedelta
from django.db.models import Q





# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            '''Begin reCaptcha'''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            '''end recaptha'''
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            category = form.cleaned_data.get('category')
            user = authenticate(username=username , password=raw_password)

            if category=='Start-up':
                group = Group.objects.get(name="Start-up")
                user.groups.add(group)
            elif category=='Buyer':
                group = Group.objects.get(name="Buyer")
                user.groups.add(group)
            elif category=='Advertiser':
                group = Group.objects.get(name="Advertiser")
                user.groups.add(group)
            elif category=='User':
                group = Group.objects.get(name="User")
                user.groups.add(group)

            login(request,user)
            return HttpResponseRedirect('home')
    else:
        form = SignUpForm()

    return render(request,'startx/signup.html',{'form':form})



def home(request):
    instance = Product.objects.all().order_by('-timestamp')
    user = request.user
    return render(request,'startx/home.html',{'user':user , 'instance':instance})

def addproduct(request):
    form = AddProductForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect('/home')
    return render(request,'startx/add_product.html',{'form':form})
def product_detail(request,instance_id):
    instance = Product.objects.get(id=instance_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        instancea = form.save(commit=False)
        instancea.product = instance
        instancea.user = request.user
        instancea.save()
        return HttpResponseRedirect(reverse('product_detail',args=(instance_id,)))
    comments = Comments.objects.filter(product=instance)

    object_viewed_signal.send(instance.__class__,instance=instance,request=request)
    return render(request,'startx/product_detail.html',{'instance':instance,'form':form,'comments':comments})
def likes(request,instance_id):
    obj = get_object_or_404(Product,id=instance_id)
    user = request.user
    if user.is_authenticated:
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
    return  HttpResponseRedirect(reverse('product_detail', args=(instance_id,)))



def dashboard(request,instance_id):
    instance = Product.objects.get(id=instance_id)

    dataset1 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=1),object_id=instance_id).count()
    dataset2 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=2),object_id=instance_id).count()
    dataset3 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=3),object_id=instance_id).count()
    dataset4 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=4),object_id=instance_id).count()
    dataset5 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=5),object_id=instance_id).count()
    dataset6 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=6),object_id=instance_id).count()
    dataset7 = ObjectView.objects.filter(timeview__gte=datetime.now()-timedelta(days=7),object_id=instance_id).count()
    context = {
        'dataset1':dataset1,
        'dataset2':dataset2,
        'dataset3':dataset3,
        'dataset4':dataset4,
        'dataset5':dataset5,
        'dataset6':dataset6,
        'dataset7':dataset7,

        }



    return render(request,'startx/dashboard.html',context)

def jobs(request):
    instance = Job.objects.all().order_by('-time')
    query = request.GET.get('jobsearch')
    if query:
        instance = Job.objects.filter(Q(job_title__icontains=query)|Q(user__profile__company_name__icontains=query))
    return render(request,'startx/job_list.html',{'instance':instance})
def add_jobs(request):
    form = AddJobForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('jobs'))
    return render(request,'startx/add_job.html',{'form':form})
def job_detail(request,instance_id):
    instance = Job.objects.get(id=instance_id)
    return render(request,'startx/job_description.html',{'instance':instance})

#Profile categorisation
def profile(request):
    user = request.user
    product1 = Product.objects.filter(user=user).count()

    instance = Product.objects.filter(user=user).order_by('likes')[:3]
    return render(request,'startx/profile.html',{'user':user,'instance':instance,'product1':product1})
def profile_setting(request):
    user = request.user
    if request.method == "POST":
        user_form = UserEditForm(request.POST or None , request.FILES or None ,instance=user)
        form = CompleteProfileForm(request.POST or None ,request.FILES or None, instance=user.profile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CompleteProfileForm(instance=user.profile)
        user_form = UserEditForm(instance=user)
    return render(request,'startx/profile_setting.html',{'user':user,'form':form,'user_form':user_form})
def profile_public_profile(request):
    user = request.user
    return render(request,'startx/profile_public_profile.html',{'user':user})
def profile_product(request):
    user = request.user
    #instance = Product.objects.get(user=user)
    return render(request,'startx/profile_product.html',{'user':user,})
def profile_jobs(request):
    user = request.user
    instance = Job.objects.filter(user=user)
    return render(request,'startx/profile_jobs.html',{'instance':instance,'user':user})
def profile_stock(request):
    user = request.user
    #instance = Product.objects.get(user=user)
    return render(request,'startx/profile_stock.html',{'user':user,})


#Advertiser
def advertisement(request):
    instance = Advertisement.objects.all()
    return render(request,'startx/advertisement.html',{'instance':instance})
def add_advertisement(request):
    form = AddAdvertisementForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('advertisement'))
    return render(request,'startx/add_advertisement.html',{'form':form})

#Guide
def guide(request):
    return render(request,'startx/guide.html')

#Product categorisation
def product_categories(request):
    return render(request,'startx/product_categories.html')
def technology_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Technology'))
    return render(request,'startx/product_categories_technology.html',{'instance':instance})
def vehicle_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Vehicles'))
    return render(request,'startx/product_categories_vehicle.html',{'instance':instance})
def sports_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Sports'))
    return render(request,'startx/product_categories_sports.html',{'instance':instance})
def audio_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Audio'))
    return render(request,'startx/product_categories_audio.html',{'instance':instance})
def furniture_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Furniture'))
    return render(request,'startx/product_categories_furniture.html',{'instance':instance})
def clothing_category(request):
    instance = Product.objects.filter(Q(product_category__contains='Clothing'))
    return render(request,'startx/product_categories_clothing.html',{'instance':instance})


def logoutv(request):
    logout(request)
    return HttpResponseRedirect('/user-login')

def loginv(request):
    if request.method == "POST":
        form = AuthenticationLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationLoginForm(request)

    return render(request,'registration/login.html',{'form':form})
