from django.db import models
from pytz import timezone

from settings.debug import TIME_ZONE


class SystemInfo(models.Model):
    cpu_avg = models.FloatField(verbose_name="текущая загрузка процессора")
    created = models.DateTimeField(verbose_name="Дата создания записи", auto_now=True)

    def get_str_data(self) -> str:
        dt_with_timezone = self.created.astimezone(tz=timezone(TIME_ZONE))
        return f"{dt_with_timezone.day}.{dt_with_timezone.month}.{dt_with_timezone.year}\
                    {dt_with_timezone.hour}:{dt_with_timezone.minute}:{dt_with_timezone.second}"

    class Meta:
        verbose_name = "Информация о системе"
        verbose_name_plural = "Записи о состоянии системы"
