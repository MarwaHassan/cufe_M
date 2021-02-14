from django.db import models
# from datetime import datetime
from django.utils import timezone


def get_year_choices(is_acad=False):
    curr_year = timezone.now().year
    year_choices = []
    for i in range(-20, 7):
        if is_acad:
            y1 = curr_year + i - is_acad
            y2 = y1 + 1
            year_choices.append((y2, '%s-%s' % (y1, y2)))
        else:
            y = curr_year + i
            year_choices.append((y, y))
    return year_choices


def get_monthly_choices():
    import calendar
    return [(str(k), v) for k, v in enumerate(calendar.month_abbr)][1:13]


monthly_choices_ara = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو',
                       'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر']

monthly_choices = [(1,'يناير'), (2,  'فبراير'),  (3, 'مارس'),  (4, 'أبريل'),  (5, 'مايو'),  (6, 'يونيو'), (7, 'يوليو'),  (8, 'أغسطس'),  (9, 'سبتمبر'),  (10, 'أكتوبر'),  (11, 'نوفمبر'),  (12, 'ديسمبر')]


grade_choices = [(0, 'الإعدادية'), (1, 'الأولى'), (2, 'الثانية'), (3, 'الثالثة'), (4, 'الرابعة')]
semester_choices = [('fall', 'خريف'), ('spring', 'ربيع'), ('summer', 'صيف')]
quarterly_choices = [('q1', 'أول'), ('q2', 'ثان'), ('q3', 'ثالث'), ('q4', 'رابع')]
quarterly_choices_ara = ['أول', 'ثان', 'ثالث', 'رابع']

biannual_choices = [('h1', 'أول'), ('h2', 'ثان')]
biannual_choices_ara = ['أول', 'ثان']


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CufeEntityType(models.Model):
    entity_type_id = models.AutoField(primary_key=True)
    entity_type_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_entity_type'

    def __str__(self):
        return self.entity_type_name


class CufeEntities(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)
    ent_email1 = models.CharField(max_length=32)
    ent_email2 = models.CharField(max_length=32)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    approv_user_id = models.IntegerField()
    entity_type = models.ForeignKey('CufeEntityType', models.DO_NOTHING)
    accepts_ext_trans = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cufe_entities'

    def __str__(self):
        return self.ent_fullname


class CufeEntityItems(models.Model):
    ent_item_id = models.AutoField(primary_key=True)
    ent_item_name = models.CharField(max_length=512)
    ent = models.ForeignKey('CufeEntities', models.DO_NOTHING)
    is_form = models.IntegerField()
    form_class = models.CharField(max_length=64)
    fold_subpath = models.CharField(max_length=512)
    is_attach_optional = models.IntegerField()
    last_added = models.DateField()
    last_notification_date = models.DateField()                                     #by Marwa

    class Meta:
        managed = False
        db_table = 'cufe_entity_items'

    def __str__(self):
        return self.ent_item_name


class CufeUserItems(models.Model):
    user_id = models.IntegerField()
    approv_user_id = models.IntegerField()
    ent_item_id = models.AutoField(primary_key=True)
    ent_item_name = models.CharField(max_length=512)
    is_form = models.IntegerField()
    form_class = models.CharField(max_length=64)
    last_added = models.DateField()
    fold_subpath = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'cufe_user_items'

    def __str__(self):
        return self.ent_item_name

class CufeApprovUserItems(models.Model):
    user_id = models.IntegerField()
    ent_item_id = models.AutoField(primary_key=True)
    ent_item_name = models.CharField(max_length=512)
    is_form = models.IntegerField()
    form_class = models.CharField(max_length=64)
    last_added = models.DateField()
    fold_subpath = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'cufe_approv_user_items'

    def __str__(self):
        return self.ent_item_name

class CufeDepartments(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cufe_departments'

    def __str__(self):
        return self.ent_fullname


class CufeDepartmentsExtTrans(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_departments_ext_trans'

    def __str__(self):
        return self.ent_fullname


class CufeFacDegrees(models.Model):
    fac_deg_id = models.IntegerField(primary_key=True)
    fac_deg_fullname = models.CharField(max_length=32)
    fac_deg_shortname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_fac_degrees'

    def __str__(self):
        return self.fac_deg_fullname


class CufeItemPeriods(models.Model):
    item_period_id = models.AutoField(primary_key=True)
    entity_item = models.ForeignKey('CufeEntityItems', on_delete=models.CASCADE)
    item_period = models.CharField(max_length=16)
    next_deadline = models.DateField()
    notification_period = models.CharField(max_length=16)
    next_notification_Date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_item_periods'


class CufeLegalEmployees(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    wrangle_cnt = models.IntegerField(verbose_name='مشادة')
    absence_cnt = models.IntegerField(verbose_name='غياب')
    commit_lack_cnt = models.IntegerField(verbose_name='عدم التزام بالتعليمات')
    financial_cnt = models.IntegerField(verbose_name='مالي')
    harass_cnt = models.IntegerField(verbose_name='تحرش')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_legal_employees'


class CufeLegalStudents(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    cheating_cnt = models.IntegerField(verbose_name='غش')
    wrangle_cnt = models.IntegerField(verbose_name='مشادة')
    commit_lack_cnt = models.IntegerField(verbose_name='عدم التزام بالتعليمات')
    harass_cnt = models.IntegerField(verbose_name='تحرش')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_legal_students'


class CufeLibHr(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeDepartments', models.DO_NOTHING, verbose_name='تخصص العاملين بالمكتبة')
    emp_cnt = models.IntegerField(verbose_name='عددهم في التخصص')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_lib_hr'


class CufeLibResources(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    capacity = models.IntegerField(verbose_name='الطاقة الاستيعابية (عدد الطلاب)')
    computers_cnt = models.IntegerField(verbose_name='عدد اجهزة الكمبيوتر')
    photocopy_cnt = models.IntegerField(verbose_name='عدد ماكينات التصوير')
    scanners_cnt = models.IntegerField(verbose_name='عدد اجهزة المسح الضوئي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_lib_resources'


class CufeLibScientificRes(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeDepartments', models.DO_NOTHING, verbose_name='التخصص')
    ref_ar_cnt = models.IntegerField(verbose_name='عدد المراجع العلمية العربية ')
    ref_en_cnt = models.IntegerField(verbose_name='عدد المراجع العلمية الاجنبية')
    printed_pub_cnt = models.IntegerField(verbose_name='عدد الدوريات المطبوعة')
    master_cnt = models.IntegerField(verbose_name='عدد رسائل الماجيستير')
    phd_cnt = models.IntegerField(verbose_name='عدد رسائل الدكتوراه')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_lib_scientific_res'


class CufeLibVisitorsCnt(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartments', models.DO_NOTHING, verbose_name='التخصص')
    ug_cnt = models.IntegerField(verbose_name='عدد الطلاب المترددين بنظام البكالوريوس')
    pg_cnt = models.IntegerField(verbose_name='عدد الطلاب المترددين بنظام الدراسات العليا')
    fac_cnt = models.IntegerField(verbose_name='عدد اعضاء هيئة التدريس')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_lib_visitors_cnt'


class CufeLocationType(models.Model):
    loc_type_id = models.AutoField(primary_key=True)
    location_type_name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cufe_location_type'

    def __str__(self):
        return self.location_type_name


class CufeMaintenanceType(models.Model):
    maint_type_id = models.AutoField(primary_key=True)
    maint_name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cufe_maintenance_type'

    def __str__(self):
        return self.maint_name


class CufeMaintDevices(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_maint_devices'

    def __str__(self):
        return self.device_name


class CufeEngMaintenance(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    period = models.IntegerField(verbose_name='الشهر', choices=monthly_choices)
    day = models.IntegerField(verbose_name='اليوم', choices=[(d, str(d)) for d in range(1,32)])
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    location = models.CharField(max_length=256, verbose_name='المكان')
    loc_type = models.ForeignKey('CufeLocationType', verbose_name='نوع المكان', on_delete=models.CASCADE)
    device = models.ForeignKey('CufeMaintDevices', verbose_name='الجهاز', on_delete=models.CASCADE)
    model = models.CharField(max_length=128, verbose_name='النوع')
    performance = models.CharField(max_length=512, verbose_name='القدرة')
    maint_type = models.ForeignKey('CufeMaintenanceType', verbose_name='الأعمال', on_delete=models.CASCADE)
    prev_maint_date = models.DateField(verbose_name='تاريخ الصيانة السابقة')
    next_maint_date = models.DateField(verbose_name='تاريخ الصيانة القادمة')
    duration = models.CharField(max_length=32, verbose_name='مدة الصيانة الدورية')
    maint_reason = models.TextField(verbose_name='سبب الصيانة قبل انتهاء المدة')
    approved = models.IntegerField(default=0, editable=False, verbose_name='موثق')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_eng_maintenance'


class CufeMaintMaintenance(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    period = models.IntegerField(verbose_name='الشهر', choices=monthly_choices)
    day = models.IntegerField(verbose_name='اليوم', choices=[(d, str(d)) for d in range(1,32)])
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    location = models.CharField(max_length=256, verbose_name='المكان')
    loc_type = models.ForeignKey('CufeLocationType', verbose_name='نوع المكان', on_delete=models.CASCADE)
    device = models.ForeignKey('CufeMaintDevices', verbose_name='الجهاز', on_delete=models.CASCADE)
    model = models.CharField(max_length=128, verbose_name='النوع')
    performance = models.CharField(max_length=512, verbose_name='القدرة')
    maint_type = models.ForeignKey('CufeMaintenanceType', verbose_name='الأعمال', on_delete=models.CASCADE)
    prev_maint_date = models.DateField(verbose_name='تاريخ الصيانة السابقة')
    next_maint_date = models.DateField(verbose_name='تاريخ الصيانة القادمة')
    duration = models.CharField(max_length=32, verbose_name='مدة الصيانة الدورية')
    maint_reason = models.TextField(verbose_name='سبب الصيانة قبل انتهاء المدة')
    approved = models.IntegerField(default=0, editable=False, verbose_name='موثق')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_maint_maintenance'


class CufePeriodTypes(models.Model):
    period_type_id = models.IntegerField(primary_key=True)
    period_type_name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cufe_period_types'


class CufePersAffairsEmployees(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    total_cnt = models.IntegerField(verbose_name='عدد العاملين')
    field_cnt = models.IntegerField(verbose_name='عدد الذين يعملون بتخصصهم')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_pers_affairs_employees'


class CufePersAffairsFaculty(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    fac_deg = models.ForeignKey('CufeFacDegrees', verbose_name='الدرجة العلمية', on_delete=models.CASCADE)
    total_cnt = models.IntegerField(verbose_name='العدد الكلي')
    active_cnt = models.IntegerField(verbose_name='على رأس العمل')
    inactive_cnt = models.IntegerField(verbose_name='اجازة')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_pers_affairs_faculty'


class CufePostAffairsForeign(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    period = models.CharField(max_length=12, verbose_name='الفصل الدراسي', choices=semester_choices)
    prog_deg = models.ForeignKey('CufeProgDegrees', verbose_name='الدرجة', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    adm_cnt = models.IntegerField(verbose_name='عدد الطلاب الوافدين الحاصلين على قبول مبدأي')
    reg_cnt = models.IntegerField(verbose_name='عدد الطلاب الوافدين المقيدين')
    total_cnt = models.IntegerField(verbose_name='الاجمالي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_foreign'


class CufePostAffairsPrograms(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    reg_cnt = models.IntegerField(verbose_name='عدد الطلاب المقيدين')
    dept_names = models.CharField(max_length=256, verbose_name='الاقسام العلمية المشاركة')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_programs'


class CufePostAffairsResearchStuds(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    stud_name = models.IntegerField(verbose_name='اسم الطالب')
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='تاريخ البدء')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_research_studs'


class CufePostAffairsScholarships(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog_deg = models.ForeignKey('CufeProgDegrees', verbose_name='الدرجة', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    sch_cnt = models.IntegerField(verbose_name='عدد طلاب المنح')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_scholarships'


class CufePostAffairsStudents(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog_deg = models.ForeignKey('CufeProgDegrees', verbose_name='الدرجة', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    applied_cnt = models.IntegerField(verbose_name='عدد الطلاب المتقدمين')
    reg_cnt = models.IntegerField(verbose_name='عدد الطلاب المقيدين')
    total_cnt = models.IntegerField(verbose_name='الاجمالي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_students'


class CufeProcAccounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_proc_accounts'

    def __str__(self):
        return self.account_name


class CufeProcCategories(models.Model):
    entry_id = models.AutoField(primary_key=True)
    categ_name = models.CharField(max_length=256, verbose_name='التصنيف')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_proc_categories'

    def __str__(self):
        return self.categ_name


class CufeProcEntities(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)
    entity_type = models.ForeignKey('CufeEntityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cufe_proc_entities'

    def __str__(self):
        return self.ent_fullname


class CufeProcModels(models.Model):
    entry_id = models.AutoField(primary_key=True)
    categ = models.ForeignKey('CufeProcCategories', verbose_name='التصنيف', on_delete=models.DO_NOTHING)
    model_name = models.CharField(max_length=256, verbose_name='البند')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_proc_models'

    def __str__(self):
        return self.model_name


class CufeProcStock(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي',
                             on_delete=models.DO_NOTHING)
    date = models.DateField(verbose_name='التاريخ')
    categ = models.ForeignKey('CufeProcCategories', verbose_name='التصنيف',
                              to_field='entry_id', on_delete=models.DO_NOTHING)
    model = models.ForeignKey('CufeProcModels', verbose_name='البند', to_field='entry_id',
                              on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(verbose_name='الكمية')
    ent_type = models.ForeignKey('CufeEntityType', verbose_name='الجهة',
                                 on_delete=models.DO_NOTHING)
    ent = models.ForeignKey('CufeProcEntities', verbose_name='القسم/المركز/المعمل',
                            on_delete=models.DO_NOTHING)
    approved = models.IntegerField(default=0, editable=False, verbose_name='موثق')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_proc_stock'


class CufeProcPurchases(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='التاريخ')
    categ = models.ForeignKey('CufeProcCategories', verbose_name='التصنيف', to_field='entry_id', on_delete=models.DO_NOTHING)
    model = models.ForeignKey('CufeProcModels', verbose_name='البند', to_field='entry_id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(verbose_name='الكمية')
    ent_type = models.ForeignKey('CufeEntityType', verbose_name='الجهة', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeProcEntities', verbose_name='القسم/المركز/المعمل', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='القيمة')
    account = models.ForeignKey('CufeProcAccounts', verbose_name='جهة الصرف', on_delete=models.CASCADE)
    approved = models.IntegerField(default=0, editable=False, verbose_name='موثق')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_proc_purchases'


class CufeProgDegrees(models.Model):
    prog_deg_id = models.AutoField(primary_key=True)
    prog_deg_fullname = models.CharField(max_length=128)
    prog_deg_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cufe_prog_degrees'

    def __str__(self):
        return self.prog_deg_fullname


class CufeProgGrades(models.Model):
    prog_grade_id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_prog_grades'

    def __str__(self):
        return self.grade_name

class CufePrograms(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)
    is_prog = models.IntegerField()
    is_ug = models.IntegerField()
    is_chs = models.IntegerField()
    is_subprog = models.IntegerField()
    is_pg = models.IntegerField()
    is_phd = models.IntegerField()
    is_ms = models.IntegerField()
    is_ms_inter = models.IntegerField()
    is_diploma = models.IntegerField()
    is_diploma_inter = models.IntegerField()
    is_disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cufe_programs'

    def __str__(self):
        return self.prog_name


class CufePgPrograms(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_pg_programs'

    def __str__(self):
        return self.prog_name


class CufeUgPrograms(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_ug_programs'

    def __str__(self):
        return self.prog_name

class CufeProgram2Sem(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_program_2sem'

    def __str__(self):
        return self.prog_name


class CufeProgram2SemAllsub(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_program_2sem_allsub'

    def __str__(self):
        return self.prog_name


class CufeProgramsChs(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_programs_chs'

    def __str__(self):
        return self.prog_name


class CufeProgramsRanking(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_programs_ranking'

    def __str__(self):
        return self.prog_name


class CufeYears(models.Model):
    year_id = models.AutoField(primary_key=True)
    year_name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_years'

    def __str__(self):
        return self.year_name


# class CufeAttachments(models.Model):
#     attach_id = models.AutoField(primary_key=True)
#     year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
#     period = models.CharField(blank=True, max_length=16, verbose_name='الفترة')
#     created_at = models.DateField(auto_now_add=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cufe_attachments'

# def __init__(self, year_choices, period_choices,  *args, **kwargs):
#     self._meta.get_field_by_name('choices_f')[0]._choices = get_


def get_attach_model(year_choices, period_choices):
    class MyAttachModel(models.Model):
        attach_id = models.AutoField(primary_key=True)
        item = models.ForeignKey('CufeEntityItems', on_delete=models.CASCADE)
        year = models.IntegerField(blank=True, verbose_name='العام', choices=year_choices)
        period = models.CharField(blank=True, max_length=16, verbose_name='الفترة', choices=period_choices)
        created_at = models.DateField(auto_now_add=True)

        class Meta:
            managed = False
            db_table = 'cufe_attachments'

    return MyAttachModel


class CufeChsAdmissionThresholds(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufeProgramsChs', verbose_name='البرنامج', on_delete=models.CASCADE)
    thresh = models.DecimalField(max_digits=6, verbose_name='الحد الأدنى', decimal_places=4)
    admitted_cnt = models.IntegerField(verbose_name='عدد الطلاب المقبولين')
    comments = models.TextField(blank=True, verbose_name='ملحوظات', null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_chs_admission_thresholds'


class CufeChsIntroSeminars(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=128, verbose_name='اسم النشاط')
    activity_date = models.DateField(verbose_name='التاريخ')
    days_cnt = models.IntegerField(verbose_name='عدد الأيام')
    students_cnt = models.IntegerField(verbose_name='عدد الطلاب المشاركين')
    prof_cnt = models.IntegerField(verbose_name='عدد أعضاء هيئة التدريس')
    dep_cnt = models.IntegerField(verbose_name='عدد الأقسام')
    dep_names = models.TextField(verbose_name='بيان الأقسام المشاركة')
    activity_description = models.TextField(verbose_name='ملخص')
    cost = models.DecimalField(max_digits=8, verbose_name='المبلغ المصروف', decimal_places=2)
    comments = models.TextField(blank=True, verbose_name='ملحوظات', null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_chs_intro_seminars'


class CufeCultConfAttend(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    dept = models.ForeignKey('CufeDepartments', verbose_name='القسم العلمي', on_delete=models.CASCADE)
    fac_deg = models.ForeignKey('CufeFacDegrees', verbose_name='الدرجة العلمية', on_delete=models.CASCADE)
    contrib_cnt = models.IntegerField(verbose_name='عدد المساهمات')
    comments = models.TextField(blank=True, null=True, verbose_name='ملحوظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_cult_conf_attend'


class CufeActivityTypes(models.Model):
    activity_type_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_activity_types'

    def __str__(self):
        return self.activity_name


class CufeSocialServiceTypes(models.Model):
    soc_srv_type_id = models.IntegerField(primary_key=True)
    soc_srv_type_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_social_service_types'

    def __str__(self):
        return self.soc_srv_type_name


class CufeChsTopGrad(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    period = models.CharField(max_length=12, choices=semester_choices, verbose_name='الفصل الدراسي')
    prog = models.ForeignKey('CufeProgramsChs', verbose_name='البرنامج', on_delete=models.CASCADE)
    grads_cnt = models.IntegerField(verbose_name='العدد')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_chs_top_grad'


class CufeCultConfOrg(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    conf_name = models.CharField(max_length=128, verbose_name='اسم المؤتمر')
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    conf_date = models.CharField(max_length=64, verbose_name='تاريخ المؤتمر')
    accept_papers_cnt = models.IntegerField(verbose_name='عدد الابحاث المقبولة')
    topics = models.TextField(verbose_name='موضوعات المؤتمر')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_cult_conf_org'


class CufeCultExchange(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    activity_name = models.IntegerField(verbose_name='اسم النشاط')
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    no_profs = models.IntegerField(verbose_name='عدد اعضاء هيئة التدريس المشاركين')
    no_assist = models.IntegerField(verbose_name='عدد اعضاء الهيئة المعاونة المشاركين')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_cult_exchange'


class CufeDeanNationalPrizes(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    fac_name = models.CharField(max_length=64, verbose_name='اسم عضو هيئة التدريس')
    prize = models.CharField(max_length=128, verbose_name='الجائزة')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_dean_national_prizes'


class CufeDeanRankings(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='عام التصنيف', choices=get_year_choices())
    prog = models.ForeignKey('CufeProgramsRanking', verbose_name='الكلية / اسم البرنامج', on_delete=models.CASCADE)
    rank_name = models.CharField(max_length=128, verbose_name='اسم التصنيف')
    rank = models.TextField(verbose_name='الترتيب')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_dean_rankings'


class CufeDeanVipGrads(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    vip_name = models.CharField(max_length=64, verbose_name='اسم عضو هيئة التدريس')
    vip_position = models.CharField(max_length=128, verbose_name='المنصب')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_dean_vip_grads'


class CufeFinancialCenterIncome(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي', on_delete=models.CASCADE)
    quart = models.IntegerField(verbose_name='الربع')
    ent = models.ForeignKey('CufeEntities', verbose_name='الجهة المشاركة', on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='قيمة الدخل')
    doc_date = models.DateField(verbose_name='التاريخ')
    comments = models.TextField(blank=True, null=True,
                                verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_financial_center_income'


class CufeFinancialFundedProjectsOther(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي', on_delete=models.CASCADE)
    fund_source = models.CharField(max_length=512, verbose_name='الجهة المانحة')
    proj_name = models.CharField(max_length=512, verbose_name='المشروع البحثي')
    entities = models.CharField(max_length=512, verbose_name='الجهات المشاركة')
    fund_value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='قيمة التمويل')
    duration = models.CharField(max_length=64, verbose_name='مدة المشروع')
    start_date = models.DateField(verbose_name='تاريخ بدء المشروع')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_financial_funded_projects_other'


class CufeFinancialFundedProjectsTech(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي', on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=512, verbose_name='المشروع البخثي')
    entities = models.CharField(max_length=512, verbose_name='الجهات المشاركة')
    fund_value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='قيمة التمويل')
    duration = models.CharField(max_length=64, verbose_name='مدة المشروع')
    start_date = models.DateField(verbose_name='تاريخ البدء')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_financial_funded_projects_tech'


class CufeFinancialTotals(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام المالي', on_delete=models.CASCADE)
    total_y0 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='دخل الكلية العام الحالي')
    total_y1 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='دخل الكلية العام السابق')
    total_y2 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='دخل الكلية العام قبل السابق')
    total_y3 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='دخل الكلية العام قبل قبل السابق')
    comments = models.TextField(db_column='Comments', blank=True, null=True,
                                verbose_name='الملاحظات')  # Field name made lowercase.
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_financial_totals'


class CufeForeignAffairsAccepted(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    frn_adm_cnt = models.IntegerField(verbose_name='عدد الطلاب المقبولين')
    adm_thresh = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='الحد الادني للقبول')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_foreign_affairs_accepted'


class CufeForeignAffairsActivities(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    act_name = models.CharField(max_length=512, verbose_name='اسم النشاط')
    act_date = models.DateField(verbose_name='التاريخ')
    days_cnt = models.IntegerField(verbose_name='عدد الايام')
    stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المشاركين')
    fac_cnt = models.IntegerField(verbose_name='عدد اعظاء هيئة التدريس')
    prog_cnt = models.IntegerField(verbose_name='عدد الاقسام المشاركة')
    prog_names = models.CharField(max_length=1024, verbose_name='بيان الاقسام المشاركة')
    description = models.TextField(verbose_name='ملخص النشاط')
    cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='المبلغ المصروف')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_foreign_affairs_activities'


class CufeFunds(models.Model):
    fund_id = models.AutoField(primary_key=True)
    fund_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_funds'

    def __str__(self):
        return self.fund_name

class CufeGradGrades(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    grad_month = models.ForeignKey('CufeGradMonth', verbose_name='الدور', on_delete=models.CASCADE)
    system = models.ForeignKey('CufeSystems', verbose_name='نوع البرنامج', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufeProgramsChs', verbose_name='البرنامج', on_delete=models.CASCADE)
    prog_grade = models.ForeignKey('CufeProgGrades', verbose_name='التقدير', on_delete=models.CASCADE)
    stud_cnt = models.IntegerField(verbose_name='العدد')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_grad_grades'


class CufeSystems(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_fullname = models.CharField(max_length=32)
    system_shortname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_systems'

    def __str__(self):
        return self.system_fullname


class CufeGradMonth(models.Model):
    grad_month_id = models.AutoField(primary_key=True)
    grad_month = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_grad_month'

    def __str__(self):
        return self.grad_month


class CufeResearchFacultyContr(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    pub_cnt = models.IntegerField(verbose_name='عدد الابحاث')
    contrib_value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='قيمة المساهمة الاجمالية للقسم')
    description = models.TextField(verbose_name='بيان تفصيلي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_research_faculty_contr'


class CufeResearchPrizeHolders(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    name = models.CharField(max_length=128, verbose_name='الاسم')
    fac_deg = models.ForeignKey('CufeFacDegrees', verbose_name='الدرجة العلمية', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    prize = models.CharField(max_length=128, verbose_name='الجائزة/براءة الاختراع')
    # prize_date = models.DateField(verbose_name='التاريخ')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_research_prize_holders'


class CufeResearchPrizesPub(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    prize_cnt = models.IntegerField(verbose_name='عدد جوائز النشر العلمي')
    description = models.TextField(verbose_name='بيان تفصيلي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_research_prizes_pub'


class CufeResearchPrizesUni(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    prize_cnt = models.IntegerField(verbose_name='عدد جوائز الجامعة')
    description = models.TextField(verbose_name='بيان تفصيلي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_research_prizes_uni'


class CufeResearchPublications(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='العام', choices=get_year_choices())
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    inter_cnt = models.IntegerField(verbose_name='عدد الابحاث المنشورة في مجلات دولية')
    national_cnt = models.IntegerField(verbose_name='عدد الابحاث المنشورة في مجلات محلية')
    books_cnt = models.IntegerField(db_column='books_Cnt', verbose_name='عدد الكتب')  # Field name made lowercase.
    chapt_cnt = models.IntegerField(verbose_name='عدد الفصول')
    description = models.TextField(verbose_name='بيان تفصيلي')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_research_publications'


class CufeStudAffairsAdmissionThresh(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartments', verbose_name='القسم', on_delete=models.CASCADE)
    adm_thresh = models.IntegerField(verbose_name='الحد الادني')
    adm_cnt = models.IntegerField(verbose_name='عدد الطلاب المقبولين')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_admission_thresh'


class CufeStudAffairsForeignStuds(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufeProgram2SemAllsub', verbose_name='البرنامج', on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='الفرقة', choices=grade_choices)
    nationality = models.CharField(max_length=64, verbose_name='الجنسية')
    frn_cnt = models.IntegerField(verbose_name='عدد الطلاب الوافدين')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_foreign_studs'


class CufeStudAffairsHandicapped(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartments', verbose_name='القسم', on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='الفرقة', choices=grade_choices)
    stud_name = models.CharField(max_length=128, verbose_name='اسم الطالب')
    personal_info = models.CharField(max_length=512, verbose_name='البيانات الشخصية')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_handicapped'


class CufeStudAffairsIncomingTransfer(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartmentsExtTrans', verbose_name='القسم', on_delete=models.CASCADE)
    adm_cnt = models.IntegerField(verbose_name='عدد الطلاب المقبولين')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_incoming_transfer'


class CufeStudAffairsIntTransfer(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartmentsExtTrans', verbose_name='القسم', on_delete=models.CASCADE)
    adm_cnt = models.IntegerField(verbose_name='عدد الطلاب المحولين الي القسم')
    leaving_cnt = models.IntegerField(verbose_name='عدد الطلاب المحولين من القسم')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_int_transfer'


class CufeStudAffairsRegisteredStuds(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufeProgram2SemAllsub', verbose_name='البرنامج', on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='الفرقة', choices=grade_choices)
    new_cnt = models.IntegerField(verbose_name='عدد الطلاب المستجدين')
    repeat_cnt = models.IntegerField(verbose_name='عدد الطلاب الباقيين')
    ext_cnt = models.IntegerField(verbose_name='عدد الطلاب من الخارج')
    total_cnt = models.IntegerField(verbose_name='الاجمالي')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_registered_studs'


class CufeTccdJobfair(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    jobjair_date = models.DateField(verbose_name='التاريخ')
    days_cnt = models.IntegerField(verbose_name='عدد الايام')
    company_cnt = models.IntegerField(verbose_name='عدد الشركات المشاركة')
    stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المستفيدين')
    prog_cnt = models.IntegerField(verbose_name='عدد الاقسام')
    prog_names = models.TextField(verbose_name='بيان الاقسام المشاركة')
    description = models.TextField(verbose_name='ملخص الحدث')
    cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='المبلغ المصروف')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_tccd_jobfair'


class CufeTrainStats(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    comp_cnt = models.IntegerField(verbose_name='عدد الشركات التي تم التعاون معها')
    train_type = models.ForeignKey('CufeTrainTypes', verbose_name='نوع التدريب', on_delete=models.CASCADE)
    stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المستفيدين')
    departments = models.CharField(max_length=512, verbose_name='الأقسام')
    comments = models.TextField(blank=True, null=True, verbose_name='الملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_train_stats'


class CufeTrainTypes(models.Model):
    train_type_id = models.AutoField(primary_key=True)
    train_type_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cufe_train_types'

    def __str__(self):
        return self.train_type_name


class CufeVdEnvSeminars(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    seminar_name = models.CharField(max_length=256, verbose_name='اسم النشاط')
    date = models.DateField(verbose_name='تاريخ النشاط')
    days_cnt = models.IntegerField(verbose_name='عدد الأيام')
    prog_id = models.ForeignKey('CufeUgPrograms', verbose_name='القسم المنظم',  on_delete=models.CASCADE)
    stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المشاركين')
    fac_cnt = models.IntegerField(verbose_name='عدد أعضاء هيئة التدريس')
    summary = models.TextField(verbose_name='ملخص')
    cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='المبلغ المصروف')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_vd_env_seminars'


class CufeVdPostAgreements(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    agr_name = models.IntegerField(verbose_name='اسم الاتفاقية')
    entities = models.CharField(max_length=512, verbose_name='الجهات المشاركة في الاتفاقية')
    duration = models.CharField(max_length=64, verbose_name='مدة الاتفاقية')
    agr_date = models.DateField(verbose_name='تاريخ بدء الاتفاقية')
    topic = models.CharField(max_length=128, verbose_name='موضوع الاتفاقية')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_agreements'


class CufeVdPostCertificates(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    prog = models.ForeignKey('CufePgPrograms', verbose_name='البرنامج', on_delete=models.CASCADE)
    universities = models.CharField(max_length=512, verbose_name='الجامعات المشاركة')
    cert_org = models.CharField(max_length=128, verbose_name='جهة الاعتماد')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_certificates'


class CufeVdPostDeptResPlans(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeDepartments', verbose_name='القسم', on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_dept_res_plans'


class CufeVdStudFundStudAct(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    conf_contrib_cnt = models.IntegerField(blank=True, null=True, verbose_name='عدد المساهمات لحضور مؤتمرات')
    workshop_contrib_cnt = models.IntegerField(blank=True, null=True, verbose_name='عدد المساهمات لحضور ورش عمل')
    challeng_contrib_cnt = models.IntegerField(blank=True, null=True, verbose_name='عدد المساهمات لحضور مسابقات دولية')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_vd_stud_fund_stud_act'


class CufeYouthCarePrizes(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=128, verbose_name='اسم الطالب')
    ent = models.ForeignKey('CufeEntities', verbose_name='القسم', on_delete=models.CASCADE)
    prize = models.CharField(max_length=128, verbose_name='الجائزة')
    prize_date = models.DateField(verbose_name='تاريخ الجائزة')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_prizes'


class CufeYouthCareSocialServices(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    soc_srv_type = models.ForeignKey('CufeSocialServiceTypes', verbose_name='نوع الخدمة', on_delete=models.CASCADE)
    soc_srv_name = models.CharField(max_length=512, verbose_name='اسم النشاط')
    srv_date = models.DateField(verbose_name='التاريخ')
    benef_stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المستفيدين')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='تكلفة الدعم المادي')
    fund = models.ForeignKey('CufeFunds', verbose_name='اسم الصندوق', on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_social_services'


class CufeYouthCareStudentActivities(models.Model):
    entry_id = models.AutoField(primary_key=True)
    year = models.ForeignKey('CufeYears', verbose_name='العام الدراسي', on_delete=models.CASCADE)
    act_type = models.ForeignKey('CufeActivityTypes', verbose_name='نوع النشاط', on_delete=models.CASCADE)
    act_title = models.CharField(max_length=256, verbose_name='اسم النشاط')
    act_date = models.DateField(verbose_name='التاريخ')
    days_cnt = models.IntegerField(verbose_name='عدد الايام')
    stud_cnt = models.IntegerField(verbose_name='عدد الطلاب المشاركين')
    fac_cnt = models.IntegerField(verbose_name='عدد اعضاء هيئة التدريس')
    prog_cnt = models.IntegerField(verbose_name='عدد الاقسام')
    prog_names = models.CharField(max_length=1024, verbose_name='بيان الاقسام المشاركة')
    teams = models.CharField(max_length=2048, verbose_name='الفرقة')
    summary = models.CharField(max_length=2048, verbose_name='ملخص')
    cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='المبلغ المصروف')
    comments = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_student_activities'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
