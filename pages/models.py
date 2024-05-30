from django.db import models


class ContactModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class MainPageCommentsModel(models.Model):
    person_name = models.CharField(max_length=64)
    person_profession = models.CharField(max_length=32)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person_name

    class Meta:
        verbose_name = 'Pro Comment'
        verbose_name_plural = 'Pro Comments'




