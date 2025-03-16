from django.db import models
from django.urls import reverse


# Категории новостей
class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Авторы
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя автора")
    bio = models.TextField(blank=True, verbose_name="Биография")
    photo = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Новости
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Основной текст")
    photo = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Фото новости")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name="news", verbose_name="Категория")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})


# Комментарии
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments", verbose_name="Новость")
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий от {self.author}"
