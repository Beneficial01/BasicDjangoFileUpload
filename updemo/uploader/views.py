from django.shortcuts import render, redirect
from .forms import SampleFileForm
from .models import SampleFile

def upload_file(request):
    if request.method == 'POST':
        form = SampleFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = SampleFileForm()
    files = SampleFile.objects.all().order_by('-uploaded_at')[:10]
    return render(request, 'uploader/upload.html', {'form': form, 'files': files})