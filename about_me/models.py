from django.db import models


class About(models.Model):
    desc = models.TextField(max_length=5000, null=True, blank=True, help_text="متن مورد نظر")
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False, help_text='اخرین تغیر')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, help_text='تاریخ ایجاد')
    chosen = models.BooleanField(default=False, )

