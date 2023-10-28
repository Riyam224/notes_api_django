from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Note(models.Model):
    body = models.TextField(_("body"))
    updated = models.DateTimeField(_("updated"), auto_now=True)
    created = models.DateTimeField(_("created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

        ordering = ["-updated"]

    def __str__(self):
        return str(self.body)
