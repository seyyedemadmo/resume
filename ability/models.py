from django.db import models


class Ability(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255, help_text='نام مهارت')
    desc = models.CharField(null=True, blank=True, max_length=5000, help_text='توضیحات')
    percent = models.FloatField(max_length=100, null=False, blank=False, help_text="میزان مهارت")
    visible = models.BooleanField(default=True, null=False, blank=False)

    def delete(self, using=None, keep_parents=False):
        self.visible = False
        self.save()

