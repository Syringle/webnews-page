from django.db import models

#Создаю модель
class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата добавления")

    def __str__(self):
        return self.name


class Author(models.Model):  # Перенёс выше
    name = models.CharField(max_length=255,
                            verbose_name="Имя автора")
    bio = models.TextField(blank=True,
                           verbose_name="Биография")
    photo = models.ImageField(upload_to='authors/',
                              blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Основной текст")
    photo = models.ImageField(upload_to='media')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE,
                                 related_name="news", verbose_name="Категория")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               null=True, blank=True, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата добавления")

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name="comments", verbose_name="Новость")
    author = models.CharField(max_length=100,
                              verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата добавления")

    def __str__(self):
        return f"Комментарий от {self.author}"
