# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class CufeActivityTypes(models.Model):
    activity_type_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_activity_types'


class CufeChsAdmissionThresholds(models.Model):
    thresh_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    threash = models.DecimalField(max_digits=6, decimal_places=4)
    admitted_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_chs_admission_thresholds'


class CufeChsIntroSeminars(models.Model):
    seminar_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    period = models.CharField(max_length=12)
    activity_name = models.CharField(max_length=128)
    activity_date = models.DateField()
    days_cnt = models.IntegerField()
    students_cnt = models.IntegerField()
    prof_cnt = models.IntegerField()
    dep_cnt = models.IntegerField()
    dep_names = models.TextField()
    activity_description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_chs_intro_seminars'


class CufeChsTopGrad(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    period = models.CharField(max_length=12)
    prog_id = models.IntegerField()
    grads_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_chs_top_grad'


class CufeCultConfAttend(models.Model):
    conf_attend_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    ent_item_id = models.IntegerField()
    dept_id = models.IntegerField()
    fac_deg_id = models.IntegerField()
    contrib_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_cult_conf_attend'


class CufeCultConfOrg(models.Model):
    conf_org_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    conf_name = models.CharField(max_length=128)
    ent_id = models.IntegerField()
    conf_date = models.CharField(max_length=64)
    accept_papers_cnt = models.IntegerField()
    topics = models.TextField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_cult_conf_org'


class CufeCultExchange(models.Model):
    exchange_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    activity_name = models.IntegerField()
    ent_id = models.IntegerField()
    no_profs = models.IntegerField()
    no_assist = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_cult_exchange'


class CufeDepartments(models.Model):
    ent_id = models.IntegerField()
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_departments'


class CufeDepartmentsExtTrans(models.Model):
    ent_id = models.IntegerField()
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_departments_ext_trans'


class CufeEntities(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)
    ent_email1 = models.CharField(max_length=32)
    ent_email2 = models.CharField(max_length=32)
    user_id = models.IntegerField()
    entity_type_id = models.IntegerField()
    accepts_ext_trans = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cufe_entities'


class CufeEntityItems(models.Model):
    ent_item_id = models.AutoField(primary_key=True)
    ent_item_name = models.CharField(max_length=512)
    ent_id = models.IntegerField()
    is_form = models.IntegerField()
    form_class = models.CharField(max_length=64)
    fold_subpath = models.CharField(max_length=512)
    time_period = models.DateField()
    last_added = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_entity_items'


class CufeEntityType(models.Model):
    entity_type_id = models.AutoField(primary_key=True)
    entity_type_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_entity_type'


class CufeFacDegrees(models.Model):
    fac_deg_id = models.IntegerField(primary_key=True)
    fac_deg_fullname = models.CharField(max_length=32)
    fac_deg_shortname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_fac_degrees'


class CufeFinancialCenterIncome(models.Model):
    ci_id = models.IntegerField()
    year_id = models.IntegerField()
    quart = models.IntegerField()
    ent_id = models.IntegerField()
    value = models.DecimalField(max_digits=20, decimal_places=2)
    doc_date = models.DateField()
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_financial_center_income'


class CufeFinancialFundedProjectsOther(models.Model):
    proj_o_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    fund_source = models.CharField(max_length=512)
    proj_name = models.CharField(max_length=512)
    entities = models.CharField(max_length=512)
    fund_value = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.CharField(max_length=64)
    start_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_financial_funded_projects_other'


class CufeFinancialFundedProjectsTech(models.Model):
    proj_tk_id = models.IntegerField()
    year_id = models.IntegerField()
    proj_name = models.CharField(max_length=512)
    entities = models.CharField(max_length=512)
    fund_value = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.CharField(max_length=64)
    start_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_financial_funded_projects_tech'


class CufeFinancialTotals(models.Model):
    total_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    total_y0 = models.DecimalField(max_digits=20, decimal_places=2)
    total_y1 = models.DecimalField(max_digits=20, decimal_places=2)
    total_y2 = models.DecimalField(max_digits=20, decimal_places=2)
    total_y3 = models.DecimalField(max_digits=20, decimal_places=2)
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_financial_totals'


class CufeForeignAffairsAccepted(models.Model):
    frn_adm_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    frn_adm_cnt = models.IntegerField()
    adm_thresh = models.DecimalField(max_digits=4, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_foreign_affairs_accepted'


class CufeForeignAffairsActivities(models.Model):
    frn_act_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    act_name = models.CharField(max_length=512)
    act_date = models.DateField()
    days_cnt = models.IntegerField()
    stud_cnt = models.IntegerField()
    fac_cnt = models.IntegerField()
    prog_cnt = models.IntegerField()
    prog_names = models.CharField(max_length=1024)
    description = models.TextField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_foreign_affairs_activities'


class CufeFunds(models.Model):
    fund_id = models.AutoField(primary_key=True)
    fund_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_funds'


class CufeGradGrades(models.Model):
    grade_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    grad_month_id = models.IntegerField()
    system_id = models.IntegerField()
    prog_id = models.IntegerField()
    prog_grade_id = models.IntegerField()
    stud_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_grad_grades'


class CufeGradMonth(models.Model):
    grad_month_id = models.AutoField(primary_key=True)
    grad_month = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_grad_month'


class CufeItemPeriods(models.Model):
    item_period_id = models.AutoField(primary_key=True)
    entity_item_id = models.IntegerField()
    period = models.CharField(max_length=16)
    deadline = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_item_periods'


class CufeLegalEmployees(models.Model):
    emp_stat_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    wrangle_cnt = models.IntegerField()
    absence_cnt = models.IntegerField()
    commit_lack_cnt = models.IntegerField()
    financial_cnt = models.IntegerField()
    harass_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_legal_employees'


class CufeLegalStudents(models.Model):
    stud_stat_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    cheating_cnt = models.IntegerField()
    wrangle_cnt = models.IntegerField()
    commit_lack_cnt = models.IntegerField()
    harass_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_legal_students'


class CufeLibHr(models.Model):
    hr_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    ent_id = models.IntegerField()
    emp_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_lib_hr'


class CufeLibResources(models.Model):
    res_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    capacity = models.IntegerField()
    computers_cnt = models.IntegerField()
    photocopy_cnt = models.IntegerField()
    scanners_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_lib_resources'


class CufeLibScientificRes(models.Model):
    sci_res_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    ent_id = models.IntegerField()
    ref_ar_cnt = models.IntegerField()
    ref_en_cnt = models.IntegerField()
    printed_pub_cnt = models.IntegerField()
    master_cnt = models.IntegerField()
    phd_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_lib_scientific_res'


class CufeLibVisitorsCnt(models.Model):
    visit_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    ug_cnt = models.IntegerField()
    pg_cnt = models.IntegerField()
    fac_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_lib_visitors_cnt'


class CufePeriodTypes(models.Model):
    period_type_id = models.IntegerField(primary_key=True)
    period_type_name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cufe_period_types'


class CufePersAffairsEmployees(models.Model):
    emp_id = models.IntegerField()
    year = models.IntegerField()
    total_cnt = models.IntegerField()
    field_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_pers_affairs_employees'


class CufePersAffairsFaculty(models.Model):
    aca_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    fac_deg_id = models.IntegerField()
    total_cnt = models.IntegerField()
    active_cnt = models.IntegerField()
    inactive_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_pers_affairs_faculty'


class CufePostAffairsForeign(models.Model):
    pg_frn_id = models.IntegerField()
    year_id = models.IntegerField()
    period = models.CharField(max_length=12)
    prog_deg_id = models.IntegerField()
    prog_id = models.IntegerField()
    adm_cnt = models.IntegerField()
    reg_cnt = models.IntegerField()
    total_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_foreign'


class CufePostAffairsPrograms(models.Model):
    pg_prog_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    reg_cnt = models.IntegerField()
    dept_names = models.CharField(max_length=256)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_programs'


class CufePostAffairsResearchStuds(models.Model):
    res_id = models.IntegerField()
    year_id = models.IntegerField()
    stud_name = models.IntegerField()
    prog_id = models.IntegerField()
    start_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_research_studs'


class CufePostAffairsScholarships(models.Model):
    scholar_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_deg_id = models.IntegerField()
    prog_id = models.IntegerField()
    sch_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_scholarships'


class CufePostAffairsStudents(models.Model):
    reg_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_deg_id = models.IntegerField()
    prog_id = models.IntegerField()
    applied_cnt = models.IntegerField()
    reg_cnt = models.IntegerField()
    total_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_post_affairs_students'


class CufeProcAccounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cufe_proc_accounts'


class CufeProcStock(models.Model):
    stock_id = models.IntegerField()
    year_id = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length=128)
    item = models.CharField(max_length=128)
    quantity = models.IntegerField()
    ent_type_id = models.IntegerField()
    ent_id = models.IntegerField()
    comments = models.IntegerField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_proc_stock'


class CufeProgDegrees(models.Model):
    prog_deg_id = models.AutoField(primary_key=True)
    prog_deg_fullname = models.CharField(max_length=128)
    prog_deg_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cufe_prog_degrees'


class CufeProgGrades(models.Model):
    prog_grade_id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_prog_grades'


class CufeProgram2Sem(models.Model):
    prog_id = models.IntegerField()
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_program_2sem'


class CufeProgram2SemAllsub(models.Model):
    prog_id = models.IntegerField()
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_program_2sem_allsub'


class CufePrograms(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)
    is_chs = models.IntegerField()
    is_subprog = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cufe_programs'


class CufeProgramsChs(models.Model):
    prog_id = models.IntegerField()
    prog_name = models.CharField(max_length=64)
    prog_code = models.CharField(max_length=12)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_programs_chs'


class CufeResearchFacultyContr(models.Model):
    contr_id = models.IntegerField()
    year = models.IntegerField()
    ent_id = models.IntegerField()
    pub_cnt = models.IntegerField()
    contrib_value = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_research_faculty_contr'


class CufeResearchPrizeHolders(models.Model):
    pr_hld_id = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=128)
    fac_deg_id = models.IntegerField()
    ent_id = models.IntegerField()
    prize = models.CharField(max_length=128)
    prize_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_research_prize_holders'


class CufeResearchPrizesPub(models.Model):
    pr_pub_id = models.IntegerField()
    year = models.IntegerField()
    ent_id = models.IntegerField()
    prize_cnt = models.IntegerField()
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_research_prizes_pub'


class CufeResearchPrizesUni(models.Model):
    pr_uni_id = models.IntegerField()
    year = models.IntegerField()
    ent_id = models.IntegerField()
    prize_cnt = models.IntegerField()
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_research_prizes_uni'


class CufeResearchPublications(models.Model):
    pub_id = models.IntegerField()
    year = models.IntegerField()
    ent_id = models.IntegerField()
    inter_cnt = models.IntegerField()
    national_cnt = models.IntegerField()
    books_cnt = models.IntegerField(db_column='books_Cnt')  # Field name made lowercase.
    chapt_cnt = models.IntegerField()
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_research_publications'


class CufeSocialServiceTypes(models.Model):
    soc_srv_type_id = models.IntegerField(primary_key=True)
    soc_srv_type_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_social_service_types'


class CufeStudAffairsAdmissionThresh(models.Model):
    thresh_id = models.IntegerField()
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    adm_thresh = models.IntegerField()
    adm_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_admission_thresh'


class CufeStudAffairsForeignStuds(models.Model):
    frn_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    grade = models.IntegerField()
    nationality = models.CharField(max_length=64)
    frn_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_foreign_studs'


class CufeStudAffairsHandicapped(models.Model):
    hand_id = models.IntegerField()
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    grade = models.IntegerField()
    stud_name = models.CharField(max_length=128)
    personal_info = models.CharField(max_length=512)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_handicapped'


class CufeStudAffairsIncomingTransfer(models.Model):
    incom_id = models.IntegerField()
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    adm_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_incoming_transfer'


class CufeStudAffairsIntTransfer(models.Model):
    int_id = models.IntegerField()
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    adm_cnt = models.IntegerField()
    leaving_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_int_transfer'


class CufeStudAffairsRegisteredStuds(models.Model):
    reg_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    grade = models.IntegerField()
    new_cnt = models.IntegerField()
    repeat_cnt = models.IntegerField()
    ext_cnt = models.IntegerField()
    total_cnt = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_stud_affairs_registered_studs'


class CufeSystems(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_fullname = models.CharField(max_length=32)
    system_shortname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_systems'


class CufeTccdJobfair(models.Model):
    fair_id = models.IntegerField()
    year_id = models.IntegerField()
    jobjair_date = models.DateField()
    days_cnt = models.IntegerField()
    company_cnt = models.IntegerField()
    stud_cnt = models.IntegerField()
    prog_cnt = models.IntegerField()
    prog_names = models.TextField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_tccd_jobfair'


class CufeUserItems(models.Model):
    user_id = models.IntegerField()
    ent_item_id = models.IntegerField()
    ent_item_name = models.CharField(max_length=512)
    is_form = models.IntegerField()
    form_class = models.CharField(max_length=64)
    fold_subpath = models.CharField(max_length=512)
    time_period = models.DateField()
    last_added = models.DateField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cufe_user_items'


class CufeVdPostAgreements(models.Model):
    agr_id = models.IntegerField()
    year_id = models.IntegerField()
    agr_name = models.IntegerField()
    entities = models.CharField(max_length=512)
    duration = models.CharField(max_length=64)
    agr_date = models.DateField()
    topic = models.CharField(max_length=128)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_agreements'


class CufeVdPostCertificates(models.Model):
    cert_id = models.IntegerField()
    year_id = models.IntegerField()
    prog_id = models.IntegerField()
    universities = models.CharField(max_length=512)
    cert_org = models.CharField(max_length=128)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_certificates'


class CufeVdPostDeptResPlans(models.Model):
    plan_id = models.IntegerField()
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_vd_post_dept_res_plans'


class CufeVdStudFundStudAct(models.Model):
    fund_stud_act_id = models.IntegerField(primary_key=True)
    year_id = models.IntegerField()
    ent_id = models.IntegerField()
    conf_contrib_cnt = models.IntegerField(blank=True, null=True)
    workshop_contrib_cnt = models.IntegerField(blank=True, null=True)
    challeng_contrib_cnt = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_vd_stud_fund_stud_act'


class CufeYears(models.Model):
    year_id = models.AutoField(primary_key=True)
    year_name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_years'


class CufeYouthCarePrizes(models.Model):
    prize_id = models.IntegerField()
    year_id = models.IntegerField()
    student_name = models.CharField(max_length=128)
    ent_id = models.IntegerField()
    prize = models.CharField(max_length=128)
    prize_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_prizes'


class CufeYouthCareSocialServices(models.Model):
    soc_srv_id = models.IntegerField()
    year_id = models.IntegerField()
    soc_srv_type_id = models.IntegerField()
    soc_srv_name = models.CharField(max_length=512)
    srv_date = models.DateField()
    benef_stud_cnt = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    fund_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_social_services'


class CufeYouthCareStudentActivities(models.Model):
    stud_act_id = models.AutoField(primary_key=True)
    year_id = models.IntegerField()
    act_type_id = models.IntegerField()
    act_title = models.CharField(max_length=256)
    act_date = models.DateField()
    days_cnt = models.IntegerField()
    stud_cnt = models.IntegerField()
    fac_cnt = models.IntegerField()
    prog_cnt = models.IntegerField()
    prog_names = models.CharField(max_length=1024)
    teams = models.CharField(max_length=2048)
    summary = models.CharField(max_length=2048)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cufe_youth_care_student_activities'


class Departments(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=12)
    dept_fullname = models.CharField(max_length=128)
    dept_shortname = models.CharField(max_length=128)
    dept_email1 = models.CharField(max_length=32)
    dept_email2 = models.CharField(max_length=32)
    dept_user = models.CharField(max_length=32)
    dept_pass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departments'


class DeptFac(models.Model):
    dept_id = models.IntegerField()
    fac_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_fac'


class DeptStaff(models.Model):
    dept_id = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_staff'


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


class EmployeeStatus(models.Model):
    emp_status_id = models.AutoField(primary_key=True)
    emp_status_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'employee_status'


class EntityFac(models.Model):
    ent_id = models.IntegerField()
    fac_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entity_fac'


class EntityStaff(models.Model):
    ent_id = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entity_staff'


class Faculty(models.Model):
    fac_id = models.AutoField(primary_key=True)
    fac_name = models.CharField(max_length=128)
    fac_pos_id = models.IntegerField()
    fac_pos_date = models.DateField()
    emp_status_id = models.IntegerField()
    fac_email = models.CharField(max_length=64)
    fac_mobile1 = models.CharField(max_length=32)
    fac_mobile2 = models.CharField(max_length=32)
    fac_nat_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'faculty'


class FacultyPositions(models.Model):
    fac_pos_id = models.AutoField(primary_key=True)
    fac_pos_name = models.CharField(max_length=128)
    fac_pos_apprv = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'faculty_positions'


class LabFac(models.Model):
    lab_id = models.IntegerField()
    fac_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lab_fac'


class LabStaff(models.Model):
    lab_id = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lab_staff'


class Labs(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_code = models.CharField(max_length=12)
    lab_fullname = models.CharField(max_length=128)
    lab_shortname = models.CharField(max_length=128)
    lab_email1 = models.CharField(max_length=32)
    lab_email2 = models.CharField(max_length=32)
    lab_user = models.CharField(max_length=32)
    lab_pass = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'labs'


class ProgTypes(models.Model):
    prog_type_id = models.AutoField(primary_key=True)
    prog_type_code = models.CharField(max_length=12)
    prog_type_fullname = models.CharField(max_length=128)
    prog_type_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'prog_types'


class Programs(models.Model):
    prog_id = models.AutoField(primary_key=True)
    prog_type_id = models.IntegerField()
    prog_code = models.CharField(max_length=12)
    prog_fullname = models.CharField(max_length=128)
    prog_shortname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'programs'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_pos_id = models.IntegerField()
    emp_status_id = models.IntegerField()
    staff_name = models.CharField(max_length=128)
    staff_pos_date = models.DateField()
    staff_nat_id = models.IntegerField()
    staff_email = models.CharField(max_length=32)
    staff_mobile1 = models.CharField(max_length=32)
    staff_mobile2 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'staff'


class StaffPositions(models.Model):
    staff_pos_id = models.AutoField(primary_key=True)
    staff_pos_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'staff_positions'
