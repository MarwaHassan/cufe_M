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


class CufeDegrees(models.Model):
    degree_id = models.IntegerField(primary_key=True)
    degree_fullname = models.CharField(max_length=32)
    degree_shortname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cufe_degrees'


class CufeEntities(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_code = models.CharField(max_length=12)
    ent_fullname = models.CharField(max_length=128)
    ent_shortname = models.CharField(max_length=128)
    ent_email1 = models.CharField(max_length=32)
    ent_email2 = models.CharField(max_length=32)
    user_id = models.IntegerField()
    entity_type_id = models.IntegerField()

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


class CufeFormCultConfAttend(models.Model):
    conf_attend_id = models.AutoField(primary_key=True)
    ent_item_id = models.IntegerField()
    dept_id = models.IntegerField()
    degree_id = models.IntegerField()
    contrib_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cufe_form_cult_conf_attend'


class CufeSocialServices(models.Model):
    soc_srv_id = models.IntegerField(primary_key=True)
    soc_srv_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'cufe_social_services'


class CufeYouthCareStudentActivities(models.Model):
    stud_act_id = models.AutoField(primary_key=True)
    act_type_id = models.IntegerField()
    act_title = models.CharField(max_length=256)
    act_date = models.DateField()
    days_cnt = models.IntegerField()
    stud_cnt = models.IntegerField()
    fac_cnt = models.IntegerField()
    dept_cnt = models.IntegerField()
    dept_chs_id = models.IntegerField()
    teams = models.CharField(max_length=2048)
    summary = models.CharField(max_length=2048)

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
