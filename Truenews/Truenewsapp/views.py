from django.shortcuts import render, redirect
from .models import NewsCategory, Author, News
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View


def home_page(request):
    categories = NewsCategory.objects.all()
    authors = Author.objects.all()
    news = News.objects.all()

    context = {
        'categories': categories,
        'authors': authors,
        'news': news,
    }
    return render(request, 'home.html', context)


def category_page(request, pk):
    category = NewsCategory.objects.filter(id=pk).first()
    news_list = News.objects.filter(category=category) if category else News.objects.none()

    context = {
        'category': category,
        'news_list': news_list,
    }
    return render(request, 'category.html', context)


def news_detail(request, pk):
    news_item = News.objects.filter(id=pk).first()

    context = {
        'news': news_item,
    }
    return render(request, 'news_detail.html', context)


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user = authenticate(request, username=username, password=password)  # Аутентификация пользователя
            if user is not None:
                login(request, user)
                return redirect('/')

        context = {'form': form}
        return render(request, self.template_name, context)


# Поиск продукта
def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        searched_product = Product.objects.filter(product_name__iregex=get_product)

        if searched_product:
            context = {'products': searched_product}
            return render(request, 'result.html', context)
    return redirect('/')


# Log out
def logout_view(request):
    logout(request)
    return redirect('/')
