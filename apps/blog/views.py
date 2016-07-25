from models import Blog, Category
from django.shortcuts import render, redirect, render_to_response, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from forms import categoryForm, postForm
from datetime import datetime

# Create your views here.


def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()
    })

def view_post(request, slug):   
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def new_category(request):
	form = categoryForm()
	return render_to_response('blog/create_category.html', {
		'categories': Category.objects.all(),
		'form': form,
	})

def addCategory(request):
	if request.method == 'POST':

		form = categoryForm(request.POST)
		if form.is_valid():
			title = request.POST.get("title", "")
			slug = request.POST.get("title", "")
			cat_obj = Category(title = title, slug = slug)
			cat_obj.save()
			return HttpResponseRedirect(reverse('create_new_category'))
	else:
		messages.error(request, "Error")
	return render(request, 'blog/create_category.html', {
		'form': categoryForm()
	})

def new_post(request):
	form = postForm()
	return render_to_response('blog/create_post.html', {
		'form': form,
	})

def addPost(request):
	if request.method == 'POST':

		form = postForm(request.POST)
		if form.is_valid():
				title = request.POST.get("title", "")
				slug = request.POST.get("title", "")
				body = request.POST.get("body", "")
				posted = datetime.now()
				category = Category.objects.get(id = request.POST.get("category"))
				post_obj = Blog(title = title, slug = slug, body = body, posted = posted, category = category)
				post_obj.save()
				return HttpResponseRedirect(reverse('create_new_post'))
		else:
			return HttpResponse('Please make sure all fields are populated')
	else:
		messages.error(request, "Error")
	return render(request, 'blog/create_post.html', {
		'form': postForm()
	})

