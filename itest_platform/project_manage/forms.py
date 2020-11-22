from django import forms
from project_manage.models import Project, Module


# 优点：
# 实现一个表单变得很简单
# 缺点：
# 前后端高度融合

# class ProjectForm(forms.Form):
#     name = forms.CharField(label='名称', max_length=100)
#     describe = forms.CharField(label="描述", widget=forms.Textarea)
#     status = forms.BooleanField(label="状态", required=False)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        exclude = ['update_time', 'create_time']


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
        exclude = ['update_time', 'create_time']













