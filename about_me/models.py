from django.db import models
from django_jalali.db import models as jmodel


class About(models.Model):
    desc = models.TextField(max_length=5000, null=True, blank=True, help_text="متن مورد نظر")
    updated_at = jmodel.jDateTimeField(auto_now=True, null=False, blank=False, help_text='اخرین بروز رسانی')
    created_at = jmodel.jDateTimeField(auto_now_add=True, null=False, blank=False, help_text='تاریخ ایجاد')
    chosen = models.BooleanField(default=False, help_text='انتخاب شده')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.chosen:
            About.objects.all().update(chosen=False)
        super(About, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
