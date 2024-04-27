from django.db import models


class SystemInfo(models.Model):
    cpu_avg = models.FloatField(verbose_name="текущая загрузка процессора")
    created = models.DateTimeField(verbose_name="Дата создания записи", auto_now=True)

    class Meta:
        verbose_name = "Информация о системе"
        verbose_name_plural = "Записи о состоянии системы"
