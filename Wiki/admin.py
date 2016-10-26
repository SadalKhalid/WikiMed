from django.contrib import admin
from .models import Profile, Article,Activity


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','mobile_number']

  class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','addition_date','is_it_translated']
    ordering = ['title']
    actions = [make_published]

  def make_published(self,request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s articles were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

class ActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Activity,ActivityAdmin)