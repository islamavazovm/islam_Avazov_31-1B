from django.db.models import Q

from django.shortcuts import HttpResponse, render, redirect
from posts.models import Post, Product, Category, Review
from posts.forms import PostCreateForm , ProductCreateForm, ReviewCreateForm, CategoryCreateForm

from posts.constants import PAGINATION_LIMIT


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')
#
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()

        context_data = {
            'posts' : posts
        }

        return render(request, 'posts/posts.html', context=context_data)

def product_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        page = int(request.GET.get('page',1))
        product = Product.objects.all()
        print(page)

        max_page = product.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        if search:
            product = product.filter(Q(title__icontains=search) | Q(compound__icontains=search) )

        product = product[PAGINATION_LIMIT * (page-1): PAGINATION_LIMIT * page]

        context_product = {
            'product' : product,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'product/product.html', context=context_product)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        context_category = {
            'category' : category
        }
        return render(request, 'category/category.html', context=context_category)

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

    context_data = {
        'product' : product,
        'form': ReviewCreateForm
    }
    return render(request, 'product/detail.html',context=context_data)

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

    context_data = {
        'post': post
    }

    return render(request, 'posts/detail.html', context=context_data)

def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()

    context_data = {
        'review': review
    }
    return render(request, 'product/review.html', context=context_data)

def posts_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        forms = PostCreateForm(data,files)


        if forms.is_valid():
           Post.objects.create(**forms.cleaned_data)
           return redirect('/posts/')

        context_data = {
            'form': forms
        }
        return  render(request, 'posts/create.html',context=context_data)

def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'product/create.html', context=context_data)

    if request.method == 'POST':
        data,files = request.POST, request.FILES
        form = ProductCreateForm(data,files)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/product/')
        context_data = {
            'form': form
        }
        return render(request, 'product/create.html',context=context_data)
def review_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ReviewCreateForm
        }
        return render(request,'product/create_review.html', context=context_data)

    if request.method == 'POST':
        data,files = request.POST, request.FILES
        form = ReviewCreateForm(data,files)

        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            return redirect('/reviews/')
        context_data = {
            'form': form
        }
        return render(request,'product/create_review.html', context=context_data)

def category_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CategoryCreateForm
        }
        return render(request,'category/create.html', context=context_data)
    if request.method == 'POST':
        data,files = request.POST, request.FILES
        form = CategoryCreateForm(data,files)

    if form.is_valid():
        Category.objects.create(**form.cleaned_data)
        return render('/category/')
    context_data = {
        'form':form
    }
    return render(request,'category/create.html',context=context_data)
