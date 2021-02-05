from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from django.template.defaultfilters import slugify as django_slugify


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Client(models.Model):
    title = models.CharField('Название', max_length=150)
    # TODO найти выпадающее меню для этой строки
    city = models.CharField('Город', max_length=20)
    address = models.CharField('Адрес', max_length=255, blank=True)
    decision_maker = models.CharField('ЛПР', max_length=255, blank=True)
    phone = models.CharField('Телефон', max_length=12)
    email = models.EmailField('Электронная почта', blank=True)
    first_call = models.TextField('Первый звонок', blank=True)
    description = models.TextField('Описание/Комментарий', blank=True)
    next_call = models.TextField('Следующий звонок', blank=True)
    slug = models.SlugField('Ссылка на клиента', max_length=150, unique=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлён', auto_now=True)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE,
                                    verbose_name='Ответственный', blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('crm:client_detail',
                       args=[self.id, self.slug])
