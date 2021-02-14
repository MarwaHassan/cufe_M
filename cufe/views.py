from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django_tables2 import RequestConfig
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import HttpResponseRedirect, reverse
from cufe.models import CufeUserItems, CufeEntities, CufeEntityItems, CufeItemPeriods, \
    get_attach_model, get_year_choices, get_monthly_choices, CufeProcModels, \
    CufeProcEntities, CufeApprovUserItems, CufeStudAffairsIncomingTransfer, CufeDepartmentsExtTrans, \
    CufeStudAffairsIntTransfer, CufeStudAffairsRegisteredStuds, CufeProgram2SemAllsub, CufePostAffairsStudents, \
    CufeChsAdmissionThresholds, CufePrograms, CufeProgramsChs, AuthUser
from datetime import date, datetime
import cufe.models
import cufe.forms
import os
import simplejson
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from cufe.tables import UserItemsTable
from django.core.mail import send_mail
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail

from django.core import mail

# def view_user_items(request):
#     if not request.user.is_authenticated:
#         # return HttpResponseRedirect(reverse('landing_page'))  # or http response
#         return HttpResponseRedirect('/accounts/login')  # or http response
#     table = UserItemsTable(CufeUserItems.objects.filter(user_id=request.user.id))
#     RequestConfig(request).configure(table)
#     return render(request, 'items/useritems.html', {'table': table})

def qs_to_vals(qs, fields, edit_approv_mode):
    table = []
    approv_column = -1
    for row in qs:
        t = [row.entry_id]

        for i, f in enumerate(fields):
            # fn = str(f).split('.')[-1]
            val = getattr(row, f)

            if f == 'approved':
                status = int(val)
                if status == 0 and edit_approv_mode == 2:
                    val = -row.entry_id
                approv_column = i

            t.append(val)

        if edit_approv_mode == 1 and status == 1: # approved and editing user
            t[0] = 0            # do not allow editing

        table.append(t)

    return table, approv_column





def view_user_items(request):
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('landing_page'))  # or http response
        return HttpResponseRedirect(reverse('login'))  # or http response

    from django.db.models import Q
    user_id = request.user.id
    entity = CufeEntities.objects.get(Q(user=user_id) | Q(approv_user_id=user_id))

    table = CufeUserItems.objects.filter(user_id=user_id).order_by('-is_form')
    if table.count() == 0:
        table = CufeApprovUserItems.objects.filter(user_id=user_id).order_by('-is_form')

    ent_subpath = entity.ent_shortname

    for r in table:
        subpath = ent_subpath + '/' + r.fold_subpath
        check_fold(subpath)

    return render(request, 'items/useritems.html',
                  {'table': table,
                   'ent_subpath': ent_subpath,
                   'title': entity.ent_fullname})



import django_tables2 as tables


def view_item_entries2(request, item_id):
    class MyTableView(tables.SingleTableView):
        table_class = get_item_entries_table(item_id)
        model = table_class._meta.model
        template_name = "items/itementries2.html"
    return MyTableView.as_view()(request)


def get_category_models(request, categ_id):
    import simplejson
    from django.http import HttpResponse
    models = CufeProcModels.objects.filter(categ=categ_id)
    models_dict = {'null': '---------'}
    for model in models:
        models_dict[model.entry_id] = model.model_name
    return HttpResponse(simplejson.dumps(models_dict), content_type="application/json")


def get_proc_entities(request, ent_type_id):
    entities = CufeProcEntities.objects.filter(entity_type=ent_type_id)
    ent_dict = {'null': '---------'}
    for ent in entities:
        ent_dict[ent.ent_id] = ent.ent_fullname
    return HttpResponse(simplejson.dumps(ent_dict), content_type="application/json")


def get_field_names(model):
    fields = model._meta.get_fields()
    names = [f.name for f in fields]
    return names


def approve_entry(request, item_id, entry_id):
    # entry_id = -entry_id #link has the id negative

    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('landing_page'))  # or http response
        return HttpResponseRedirect(reverse('login'))  # or http response

    user_id = request.user.id

    if not verify_user_item(user_id, item_id):
        return HttpResponseRedirect(reverse('login'))

    item_obj = CufeUserItems.objects.get(ent_item_id=item_id)
    if item_obj.approv_user_id != user_id:
        return HttpResponseRedirect(reverse('login'))

    model_class_name = item_obj.form_class
    model = getattr(cufe.models, model_class_name)

    fields = get_field_names(model)
    if 'approved' in fields:
        qs = model.objects.filter(pk=entry_id).update(approved=1)
        ret = 1
    else:
        ret = 0

    return HttpResponse(simplejson.dumps(ret), content_type="application/json")


def get_item_entries_table(item_id):
    item_obj = CufeEntityItems.objects.get(pk=item_id)
    item_name = item_obj.ent_item_name
    model_class_name = item_obj.form_class

    class MyTable(tables.Table):
        class Meta:
            model = getattr(cufe.models, model_class_name)
    return MyTable


def get_edit_approv_mode(user_id, item_id):
    qs = CufeUserItems.objects.filter(user_id=user_id, ent_item_id=item_id)
    if qs.count() > 0:
        if int(qs[0].approv_user_id) == 0:
            return 0
        return 1
    qsa = CufeApprovUserItems.objects.filter(user_id=user_id, ent_item_id=item_id)
    if qsa.count() > 0:
        return 2
    return -1


def verify_user_item(user_id, item_id):
    return get_edit_approv_mode(user_id, item_id) >= 0

def send_item_Notification(request, item_id):                     #by Marwa
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('landing_page'))  # or http response
        return HttpResponseRedirect(reverse('login'))  # or http response

    user_id = request.user.id

    if not verify_user_item(user_id, item_id):
        return HttpResponseRedirect(reverse('login'))

    item_obj = CufeEntityItems.objects.get(pk=item_id)

    last_notification_date=  item_obj.last_notification_date
    item_name = item_obj.ent_item_name

    item_obj_period=CufeItemPeriods.objects.get(entity_item=item_id)
    deadline=item_obj_period.deadline

    auth_user=AuthUser.objects.get(pk=user_id)
    user_email= auth_user.email

    if(last_notification_date is None or last_notification_date <= deadline):
        res = send_mail('hello paul', 'comment tu vas?', 'marwamahmoud@eng.cu.edu.eg',[user_email,],fail_silently= False)

    return HttpResponse('%s' % res)



def view_item_entries(request, item_id):
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('landing_page'))  # or http response
        return HttpResponseRedirect(reverse('login'))  # or http response

    user_id = request.user.id

    if not verify_user_item(user_id, item_id):
        return HttpResponseRedirect(reverse('login'))

    item_obj = CufeEntityItems.objects.get(pk=item_id)
    item_name = item_obj.ent_item_name

    model_class_name = item_obj.form_class
    model = getattr(cufe.models, model_class_name)

    column_names = []

    edit_approv_mode = get_edit_approv_mode(user_id, item_id)

    fields = get_field_names(model)
    if 'year' in fields:
        qs = model.objects.select_related().all().order_by('-year', '-entry_id')
    else:
        qs = model.objects.select_related().all().order_by('-entry_id')
    if qs.count() > 0:
        column_names = ['كود إدخال']
        exclude = ['entry_id', 'created_at', 'updated_at']
        for f in qs.values()[0]:
            if f in exclude:
                continue
            column_names.append(model._meta.get_field(f).verbose_name)
        column_names.extend(['تاريخ الإدخال', 'تاريخ التعديل'])

    (table, approv_column) = qs_to_vals(qs, fields, edit_approv_mode)

    return render(request, 'items/itementries.html',
                  {'table': table,
                   'columns': column_names,
                   'item_id': item_id,
                   'edit_approv_mode': edit_approv_mode,
                   'approv_column': approv_column+2, # shifted columns
                   # 'fold_subpath': fold_subpath,
                   'title': item_name})


def check_fold(subpath):
    media_root = getattr(
        settings,
        'MEDIA_ROOT',
        '/tmp',
    )
    path = media_root + '/' + subpath + '/'
    os.makedirs(path, exist_ok=True)

    return path


def handle_uploaded_file(subpath, f):

    path = check_fold(subpath)
    with open(path + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#
# def view_item_form(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('login'))  # or http response
#
#     submitted = False
#     module_name = "cufe.models"
#     user_id = request.user.id
#     print(request.path)
#     if request.method == 'POST':
#         if 'ent_item' not in request.POST:
#             print('No item %s' % str(request.POST))
#             return HttpResponseRedirect('/')
#
#         item_id = request.POST.get('ent_item')
#         item_name = CufeEntityItems.objects.filter(ent_item_id=item_id)[0].ent_item_name
#         form_class = CufeEntityItems.objects.filter(ent_item_id=item_id)[0].form_class + "Form"
#
#         class_ = getattr(cufe.forms, form_class)
#         form = class_(item_name, item_id, request.POST)
#         # print(form)
#         print(request.FILES)
#         if form.is_valid():
#             print('Form is valid... going to save')
#             files = request.FILES.getlist('file')
#             for f in files:
#                 handle_uploaded_file(f)
#             form.save()
#             print('Form SAVED')
#             return HttpResponseRedirect('/itemform/?item=%s&submitted=True' % item_id)
#         else:
#             print(form.errors)
#     else:
#         if 'item' not in request.GET:
#             return HttpResponseRedirect('/')
#         if 'submitted' in request.GET:
#             submitted = True
#
#         item_id = request.GET.get('item')
#         entity_obj = CufeEntityItems.objects.filter(ent_item_id=item_id)[0]
#         item_name = entity_obj.ent_item_name
#         form_class = entity_obj.form_class + "Form"
#
#         class_ = getattr(cufe.forms, form_class)
#         form = class_(item_name, item_id)
#     return render(request, 'items/form.html',
#                   {'form': form,
#                    'title': item_name,
#                    'submitted': submitted})
#
#     # return render(request, 'items/itemform.html', {'table': table, 'title': entity[0].ent_fullname})


def printVars(object):
    for i in [v for v in dir(object) if not callable(getattr(object, v))]:
        print('\n%s:' % i)
        exec('print(object.%s)\n\n' % i)


class DynamicUpdateView(UpdateView):
    template_name = 'items/form.html'
    success_url = '/'
    disp_success = False
    item_name = ''
    item_id = 0

    def dispatch(self, request, *args, **kwargs):
        path = request.path.split('/')
        self.item_id = int(path[2])

        user_id = request.user.id
        if not verify_user_item(user_id, self.item_id):
            return HttpResponseRedirect(reverse('login'))

        item_obj = CufeEntityItems.objects.get(pk=self.item_id)
        self.item_name = item_obj.ent_item_name

        model_class_name = item_obj.form_class
        self.model = getattr(cufe.models, model_class_name)
        self.form_class = cufe.forms.get_form(self.model, ['entry_id'], no_file=True)
        # self.form_class = getattr(cufe.forms, model_class_name + 'Form')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.item_name
        return context

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        if not request.user.is_authenticated or not verify_user_item(user_id, self.item_id):
            return HttpResponseRedirect(reverse('login'))
        edit_approv_mode = get_edit_approv_mode(user_id, self.item_id)
        if edit_approv_mode == 1:
            entry_obj = self.model.objects.get(pk=kwargs['pk'])
            if entry_obj.approved == 1:
                return HttpResponseRedirect(reverse('login'))
        return super().get(request, *args, **kwargs)
    #     context = {'form': self.form_class,
    #                'title': self.item_name}
    #     return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)


class DynamicCreateView(CreateView):
    template_name = 'items/form.html'
    success_url = '/'
    disp_success = False
    item_name = ''
    item_id = 0
    is_attach = 0

    def dispatch_attach(self, item_obj):
        exclude_list = ['item']
        year_choices = []
        period_choices = []

        item_periods_obj = CufeItemPeriods.objects.filter(entity_item=self.item_id)
        if item_periods_obj.count() >= 1:
            item_period = item_periods_obj[0].item_period
            if item_period == 'need':
                exclude_list.extend(['year', 'period'])
            elif item_period in ['calendar', 'two', 'five']:
                exclude_list.append('period')
                year_choices = get_year_choices()
            elif item_period in ['academic', 'fiscal']:
                year_choices = get_year_choices(True)
                exclude_list.append('period')
            elif item_period in ['monthly', 'nov']:
                year_choices = get_year_choices()
                period_choices = get_monthly_choices()
            elif item_period == 'monthly-acad':
                year_choices = get_year_choices(True)
                period_choices = get_monthly_choices()
            elif item_period == 'fall':
                year_choices = get_year_choices(True)
                period_choices = cufe.models.semester_choices
            elif item_period == 'q1':
                year_choices = get_year_choices()
                period_choices = cufe.models.quarterly_choices
            elif item_period == 'h1':
                year_choices = get_year_choices()
                period_choices = cufe.models.quarterly_choices

        # elif item_periods_obj.count() > 1:
        #     if period

        self.model = get_attach_model(year_choices, period_choices)
        self.form_class = cufe.forms.get_form(self.model, exclude_list)

    def dispatch_form(self, item_obj):
        model_class_name = item_obj.form_class
        self.model = getattr(cufe.models, model_class_name)
        self.form_class = cufe.forms.get_form(self.model, [], optional_file=item_obj.is_attach_optional)
        # self.form_class = getattr(cufe.forms, model_class_name + 'Form')

    def dispatch(self, request, *args, **kwargs):
        print(request.GET)
        path = request.path.split('/')

        self.item_id = int(path[2])
        user_id = request.user.id
        if not request.user.is_authenticated or not verify_user_item(user_id, self.item_id):
            return HttpResponseRedirect(reverse('login'))

        item_obj = CufeEntityItems.objects.get(pk=self.item_id)
        self.item_name = item_obj.ent_item_name

        self.is_attach = len(item_obj.form_class) == 0
        if self.is_attach:
            self.dispatch_attach(item_obj)
        else:
            self.dispatch_form(item_obj)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        if not request.user.is_authenticated or not verify_user_item(user_id, self.item_id):
            return HttpResponseRedirect(reverse('login'))

        path = request.path.split('/')
        if 'next' in path[1]:
            self.disp_success = True
        else:
            self.disp_success = False

        form = self.form_class()
        form.initial['item_id'] = self.item_id
        context = {'form': form,
                   'title': self.item_name,
                   'submitted': self.disp_success}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        if not request.user.is_authenticated or not verify_user_item(user_id, self.item_id):
            return HttpResponseRedirect(reverse('login'))

        form = self.form_class(request.POST)
        if form.is_valid():
            year = ''
            if 'year' in form.cleaned_data:
                year = str(form.cleaned_data['year'])
                if 'period' in form.cleaned_data and len(str(form.cleaned_data['period'])) > 0:
                    year = '%s/%s' % (year, form.cleaned_data['period'])
            item_obj = CufeEntityItems.objects.get(pk=self.item_id)
            ent_id = item_obj.ent_id
            fold_subpath = item_obj.fold_subpath
            ent_obj = CufeEntities.objects.get(pk=ent_id)
            ent_shortname = ent_obj.ent_shortname
            if year:
                path = '%s/%s/%s' % (ent_shortname, fold_subpath, year)
            else:
                path = '%s/%s' % (ent_shortname, fold_subpath)
            files = request.FILES.getlist('file')
            for f in files:
                handle_uploaded_file(path, f)

            if self.is_attach:
                form = form.save(commit=False)
                form.item_id = self.item_id
            form.save()
            CufeEntityItems.objects.filter(ent_item_id=self.item_id).update(last_added=str(date.today()))

            return HttpResponseRedirect(reverse_lazy('create-next-item', args=[self.item_id]))

        context = {'form': form,
                   'title': self.item_name}
        return render(request, self.template_name, context)


def contactus(request):
    return render(request, 'contactus.html')

def Dash_CHS(request):
    objs = CufeChsAdmissionThresholds.objects.all()
    prog_name = []
    thresh = []
    cnt = []

    for ent in objs:
        prog_name.append(ent.prog.prog_name)
        thresh.append(ent.thresh)
        cnt.append(ent.admitted_cnt)

    return render(request, 'graphs/Dash_CHS.html', context= {'title': '', 'jsonTable': {
        'prog_name': prog_name,
        'thresh': thresh,
        'cnt': cnt,
    },
    })

def Dash_SCI(request):
    # Registered post grad students across programs and degrees
    objs = CufePostAffairsStudents.objects.values('prog').order_by('prog').annotate(cnt=Count('prog'))
    prog_names = []
    deg_2 = []
    deg_3 = []
    deg_4 = []

    for ent in objs:
        prog_names.append(CufePrograms.objects.get(pk=ent['prog']).prog_name)
        cnt_2 = CufePostAffairsStudents.objects.filter(prog=ent['prog'], prog_deg=2).aggregate(Sum('applied_cnt'))[
            'applied_cnt__sum']
        if cnt_2 is None: cnt_2 = 0
        cnt_3 = CufePostAffairsStudents.objects.filter(prog=ent['prog'], prog_deg=3).aggregate(Sum('applied_cnt'))[
            'applied_cnt__sum']
        if cnt_3 is None: cnt_3 = 0
        cnt_4 = CufePostAffairsStudents.objects.filter(prog=ent['prog'], prog_deg=4).aggregate(Sum('applied_cnt'))[
            'applied_cnt__sum']
        if cnt_4 is None: cnt_4 = 0

        deg_2.append(cnt_2)
        deg_3.append(cnt_3)
        deg_4.append(cnt_4)


    return render(request, 'graphs/Dash_SCI.html', context= {'title': '', 'jsonTable': {
        'prog_names': prog_names,
        'deg_2': deg_2,
        'deg_3': deg_3,
        'deg_4': deg_4,
    }})

def Dash_STUD(request):
    # External transfer students
    objs = CufeStudAffairsIncomingTransfer.objects.all()
    departs = []
    count = []
    for ent in objs:
        departs.append(CufeDepartmentsExtTrans.objects.get(pk=ent.ent_id).ent_shortname)
        count.append(ent.adm_cnt)

    # Internal transfer students
    objs = CufeStudAffairsIntTransfer.objects.all()
    trans_departs = []
    trans_from = []
    trans_to = []
    for ent in objs:
        trans_departs.append(CufeDepartmentsExtTrans.objects.get(pk=ent.ent_id).ent_shortname)
        trans_from.append(ent.leaving_cnt)
        trans_to.append(ent.adm_cnt)

    # Student count across grades
    objs = CufeStudAffairsRegisteredStuds.objects.values('grade').annotate(stud_cnt=Sum('total_cnt'))
    grade_count = []
    for ent in objs:
        grade_count.append(ent['stud_cnt'])

    # Student count across departments
    objs = CufeStudAffairsRegisteredStuds.objects.values('prog_id').annotate(stud_cnt=Sum('total_cnt'))
    prog_name = []
    prog_count = []
    for ent in objs:
        prog_count.append(ent['stud_cnt'])
        prog_name.append(CufeProgram2SemAllsub.objects.get(pk=ent['prog_id']).prog_name)


    return render(request, 'graphs/Dash_STUD.html', context= {'title': '', 'jsonTable': {
        'count': count,
        'departments': departs,
        'trans_departs': trans_departs,
        'trans_from': trans_from,
        'trans_to': trans_to,
        'grade_count': grade_count,
        'prog_name': prog_name,
        'prog_count': prog_count,
    },
    })


def JSON_test(request):

    # Registered post grad students across programs and degrees
    objs = CufeEntityItems.objects.values('ent').order_by('ent').annotate(cnt=Count('ent'))
    ent_names = []
    ent_total_cnt = []
    ent_updated_cnt = []
    ent_updated_prcnt = []
    for ent in objs:
        i_cnt = 0
        if ent['ent'] != 0:
            ent_names.append(CufeEntities.objects.get(pk=ent['ent']).ent_shortname)
            ent_total_cnt.append(ent['cnt'])
            # get last updated dates for this ent
            this_ent = CufeEntityItems.objects.filter(ent=ent['ent'])
            for item in this_ent:
                lu_date = item.last_added
                dl_date = CufeItemPeriods.objects.get(pk=item.ent_item_id).deadline
                dl_date = date(year=date.today().year,month=dl_date.month, day=dl_date.day)
                if date.today() > dl_date and lu_date > date(year=date.today().year-1, month=dl_date.month, day=dl_date.day): i_cnt = i_cnt + 1
            ent_updated_cnt.append(i_cnt)
            ent_updated_prcnt.append(i_cnt/ent['cnt'])
    return JsonResponse({'data': {
        'ent_name': ent_names,
        'ent_total_cnt': ent_total_cnt,
        'ent_updated_cnt': ent_updated_cnt,
        'ent_updated_prcnt': ent_updated_prcnt,
    }})
#     return HttpResponse(simplejson.dumps(data), content_type="application/json")