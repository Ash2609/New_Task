from django.shortcuts import render
from .forms import ImageForm
from .models import Upload

# Create your views here.
from django.shortcuts import render
def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img =Upload.objects.all()
    return render(request,'app1/index.html',{'img':img,'form':form})