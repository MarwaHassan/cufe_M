# from django.http.response import HttpResponse
# from django.shortcuts import render
#
#
# # Create your views here.
# def index(request):
#     # return HttpResponse('Hello forms')
#     return render(request, 'forms/attach_form.html', {
#         'title': 'نموذج'
#     })
#
# from django.views.generic.edit import FormView
# from .forms import UploadFileForm
#
#
# class FileFieldView(FormView):
#     form_class = UploadFileForm
#     template_name = 'forms/attach_form.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm
# # from .models import ModelWithFileField
#
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ModelWithFileField(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'forms/attach_form.html', {'form': form})

# from django.views.generic import CreateView
# from .models import Attach
#
#
# class AttachCreateView(CreateView):
#     model = Attach
#     fields = ('name', 'email', 'job_title', 'bio', 'file')

from django.conf import settings

from filemanager import FileManager


def filemanager_view(request, path):
    extensions = ['html', 'htm', 'zip', 'rar', 'xls', 'xlsx', '7z', 'jpeg', 'jpg', 'png', 'bmp', 'gif', 'tiff', 'pdf']
    # media_root = settings.MEDIA_ROOT
    # media_root += '/' + path
    # rel_path = path
    # if '.' not in path:
    #     rel_path = ''
    #     print("Executing if cond")
    # if 'filemanager' in path:
    #     media_root = getattr(
    #         settings,
    #         'FILEMANAGER_STATIC_ROOT',
    #         '/var/www/cufe/filemanager/static/',
    #     )
    #

    if 'filemanager' in path:
        media_root = getattr(
            settings,
            'FILEMANAGER_STATIC_ROOT',
            '/var/www/cufe/filemanager/static/',
        )
        st_ind = path.index('filemanager')
        rel_path = path[st_ind:]
    else:

        if '.' in path:
            rel_path = path
            media_root = settings.MEDIA_ROOT
        else:
            media_root = settings.MEDIA_ROOT + '/' + path
            rel_path = ''

    print(rel_path)
    print(media_root)
    fm = FileManager(media_root, maxfolders=1000000, maxspace=1024 * 1024 * 1024, maxfilesize=1024 * 1024,
                         extensions=extensions)
    return fm.render(request, rel_path, media_root)
    # return fm.render(request, '', path)

