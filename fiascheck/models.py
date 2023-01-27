from django.db import models


class Fias(models.Model):
    Houseid = models.CharField('Уникальный идентификатор записи дома', max_length=200)
    Houseguid = models.CharField('Глобальный уникальный идентификатор дома', max_length=200)
    Fias_update_date = models.DateTimeField('Дата внесения (обновления) записи')
    Is_actual = models.BooleanField('Актуальность')
    Duplicate = models.CharField('Если поле заполнелно то является дублем', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.Houseid
