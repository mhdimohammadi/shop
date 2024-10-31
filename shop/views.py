from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .forms import UserRegisterForm


def profile(request):
    user = request.user
    return render(request, 'shop/profile.html', {'user': user})


def product_list(request, category_slug=None, ordering=None):
    password = "Mahdi"
    category = None
    categories = Category.objects.all()
    products = Product.objects.prefetch_related('category').all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if ordering == "recent":
        products = products.order_by('-created')
    if ordering == "old":
        products = products.order_by('created')
    elif ordering == "expensive":
        products = products.order_by('-new_price')
    elif ordering == "cheap":
        products = products.order_by('new_price')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    category = product.category
    similar_products = Product.objects.filter(category__name__in=category).exclude(id=product.id)
    return render(request, 'shop/detail.html', {'product': product, 'similar_products': similar_products})


def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
