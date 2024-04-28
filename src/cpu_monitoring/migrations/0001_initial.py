from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SystemInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cpu_avg",
                    models.FloatField(verbose_name="текущая загрузка процессора"),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата создания записи"
                    ),
                ),
            ],
            options={
                "verbose_name": "Информация о системе",
                "verbose_name_plural": "Записи о состоянии системы",
            },
        ),
    ]
