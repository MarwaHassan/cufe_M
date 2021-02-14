from django import forms
from django.forms import ModelForm
from cufe.models import CufeProcModels
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Hidden, Field
from crispy_forms.bootstrap import FormActions


class AttachField(forms.FileField):
    is_optional = 0

    def set_optional(self, is_optional):
        self.is_optional = is_optional

    def validate(self, value):
        # super().validate(value)
        print(value)


class CufeBaseForm(ModelForm):
    # required_css_class = 'required'
    file = AttachField(max_length=512, widget=forms.ClearableFileInput(attrs={'multiple': True}), label='الملف')

    class Meta:
        file = AttachField(max_length=512, widget=forms.ClearableFileInput(attrs={'multiple': True}), label='الملف')

    def __init__(self, no_file, optional_file, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.template_pack = 'bootstrap4'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        # self.helper.add_input(Submit('save', 'إدخال'))

        if optional_file:
            self.fields['file'].required = False
        if no_file:
            self.fields.pop('file')


# class CufeCultConfAttendForm(CufeBaseForm):
#     # required_css_class = 'required'
#
#     class Meta:
#         model = cufe.models.CufeCultConfAttend
#         fields = ['year',
#                   # 'ent_item',
#                   'dept', 'fac_deg', 'contrib_cnt', 'comments']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper.layout = Layout(
#             Fieldset(
#                 '',
#                 'year',
#                 # Hidden('ent_item', str(item_id)),
#                 'dept',
#                 'fac_deg',
#                 'contrib_cnt',
#                 'comments',
#                 'file',
#             ),
#             FormActions(
#                 Submit('save', 'إدخال'),
#                 HTML(' <a class="btn btn-primary" href="/">إلغاء</a>')
#             )
#         )


def get_form(model_class, exclude_list, no_file=False, optional_file=False):
    class MyForm(CufeBaseForm):
        class Meta:
            model = model_class
            exclude = exclude_list
            # exclude = []

        def __init__(self, *args, **kwargs):
            super().__init__(no_file, optional_file, *args, **kwargs)
            self.helper.layout = Layout(
                Fieldset(
                    '',
                    *self.fields,
                ),
                FormActions(
                    Submit('save', 'إدخال'),
                    HTML(' <a class="btn btn-primary" href="/">إلغاء</a>')
                )
            )
            # if 'model' in self.fields:
                # self.fields['model'].queryset = CufeProcModels.objects.filter(categ=0)
                # self.fields['model'] = forms.ChoiceField(choices={})
                # self.fields['model'] = forms.ModelChoiceField(queryset=CufeProcModels.objects.filter(categ=0))

    return MyForm

# def get_form_update(model_class, exclude_list):
#     class MyForm(ModelForm):
#         class Meta:
#             model = model_class
#             exclude = exclude_list
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.helper.layout = Layout(
#                 Fieldset(
#                     '',
#                     *self.fields,
#
#                 ),
#                 FormActions(
#                     Submit('save', 'إدخال'),
#                     HTML(' <a class="btn btn-primary" href="/">إلغاء</a>')
#                 )
#             )
#     return MyForm

# form_class = get_form(('field1', 'field2'))
# form = form_class()

# class CufeChsAdmissionThresholdsForm(CufeBaseForm):
#     # required_css_class = 'required'
#
#     class Meta:
#         model = cufe.models.CufeChsAdmissionThresholds
#         exclude = []
#         # fields = ['year', 'prog', 'thresh', 'admitted_cnt', 'comments']
#         # fields = ['year']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields = ['year', 'prog', 'thresh', 'admitted_cnt', 'comments']
#         print(self.fields)
#
#         self.helper.layout = Layout(
#             Fieldset(
#                 '',
#                 #'year', 'prog', 'thresh', 'admitted_cnt', 'comments',
#                 *self.fields,
#                 'file',
#             ),
#             FormActions(
#                 Submit('save', 'إدخال'),
#                 HTML(' <a class="btn btn-primary" href="/">إلغاء</a>')
#             )
#         )
#
#
#
# class CufeChsIntroSeminarsForm(CufeBaseForm):
#     # required_css_class = 'required'
#
#     class Meta:
#         model = cufe.models.CufeChsIntroSeminars
#         fields = ['year', 'activity_name', 'activity_date', 'days_cnt',
#                   'students_cnt', 'prof_cnt', 'dep_cnt', 'dep_names', 'activity_description',
#                   'cost', 'comments']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper.layout = Layout(
#             Fieldset(
#                 '',
#                 'year', 'activity_name', 'activity_date', 'days_cnt',
#                 'students_cnt', 'prof_cnt', 'dep_cnt', 'dep_names', 'activity_description',
#                 'cost', 'comments',
#                 'file',
#             ),
#             FormActions(
#                 Submit('save', 'إدخال'),
#                 HTML(' <a class="btn btn-primary" href="/">إلغاء</a>')
#             )
#         )
