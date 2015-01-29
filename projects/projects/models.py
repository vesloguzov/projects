from django.db import models

class Project(models.Model):
    name = models.CharField('Название проекта', max_length=1024)
    pub_date=models.DateTimeField(auto_now_add=True)
    comment=models.TextField('Комментарий', max_length=4096, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'