from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=100, verbose_name="Отдел")

    class Meta:
        verbose_name_plural = "Отдел"

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=50, verbose_name="Имя")
    middlename = models.CharField(max_length=50, verbose_name="Отчество")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="Отдел")

    class Meta:
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.username


class Equipment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Цена")
    comment = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name_plural = "Оборудования"
    
    def __str__(self):
        return self.title


class Specification(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name_plural = "Спецификация"

    def __str__(self):
        return self.title


class EquipmentList(models.Model):
    equipmentId = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Оборудования")
    specificationId = models.ForeignKey(Specification, on_delete=models.CASCADE, verbose_name="Спецификация")
    fileName = models.CharField(max_length=255, verbose_name="Названия файла")
    fileImage = models.FileField(upload_to="equipment_files/", verbose_name="Файл")
    dateCreate = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    dateModify = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    userModifyId = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Пользователь изменил")
    userDownloadId = models.ManyToManyField(CustomUser, blank=True, verbose_name="Пользователи скачали", related_name="user_download_id")
    userUploadId = models.ManyToManyField(CustomUser, blank=True, verbose_name="Пользователь загрузил", related_name="user_upload_id")

    class Meta:
        verbose_name_plural = "Список Оборудование"

    def __str__(self):
        return self.fileName 