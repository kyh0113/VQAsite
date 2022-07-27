from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django import forms
# Create your views here.

from django.views.generic.edit import CreateView

class PhotoUploadView(CreateView): 
    model = Photo # 제네릭뷰같은 경우엔 무조건 model이 필요하다
    # 어떤 내용들을 입력받을거냐
    fields=['photo'] 
    template_name="photo/upload.html"

    def form_valid(self, form): 
        form.instance.author_id = self.request.user.id
        if form.is_valid(): # 입력한 데이터가 다 올바르면
            form.instance.save()
            return redirect('photo:photo_view') 
        else:
            return self.render_to_response({'form':form})

def photo_view(request):
    photo_list = Photo.objects.all()
    return render(request, 'photo/photo.html', {'photo_list':photo_list})

def photo_detail(request, pk):
    photo=get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/detail.html', {'photo':photo})