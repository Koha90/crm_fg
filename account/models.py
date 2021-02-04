from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Этот класс связывается с пользователем сайта и расширяет его профиль
    который будет отображаться на странице. У каждого профиля своя страница. """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    position = models.CharField('Должность', max_length=30)
    about = models.TextField('О себе', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True,
                                     verbose_name='День рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True,
                              verbose_name='Фото')
    slug = models.SlugField(max_length=30, unique=True, null=True,
                            verbose_name='Ссылка на профиль')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('user',)

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('account:profile_detail',
                       args=[self.id, self.slug])
