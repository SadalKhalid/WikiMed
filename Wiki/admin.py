from django.contrib import admin
from .models import Profile, Article,Activity


class ProfileAdmin(admin.ModelAdmin):
    list_display =['ar_first_name', 'ar_middle_name','ar_last_name','mobile_number']
    class Meta:
           model = Profile

class ArticleAdmin(admin.ModelAdmin):
    list_display =['translator','en_name','addition_date','en_link']
    list_display_links=['en_link']
    list_filter =['addition_date','when_translated']
    class Meta:
        model =Article




class ActivityAdmin(admin.ModelAdmin):
    list_display =['title','start_time','end_time','date']
    class Meta:
        model=Activity


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Activity,ActivityAdmin)