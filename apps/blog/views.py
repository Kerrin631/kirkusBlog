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
			return HttpResponseRedirect(reverse('index'))
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
				return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponse('Please make sure all fields are populated')
	else:
		messages.error(request, "Error")
	return redirect(request, 'index', {
	})

def delete_post(request, slug):
	Blog.objects.filter(slug=slug).delete()
	return render(request, 'blog/index.html', {
		'categories': Category.objects.all(),
        'posts': Blog.objects.all()
	})

def delete_category(request, slug):
	Category.objects.filter(slug=slug).delete()
	return render(request, 'blog/index.html', {
		'categories': Category.objects.all(),
        'posts': Blog.objects.all()
	})

def update_post(request, slug):
	form = postForm()
	return render_to_response('blog/update_post.html', {
		'post': get_object_or_404(Blog, slug=slug),
		'form': form,
	})

def update_post_save(request, slug):
	blog = Blog.objects.get(slug=slug) 
	if request.method == 'POST':

		form = postForm(request.POST)
		if form.is_valid():
			print('FORM IS VALID FORM IS VALID')
			title = request.POST.get("title", "")
			slug = request.POST.get("title", "")
			body = request.POST.get("body", "")
			posted = datetime.now()
			category = Category.objects.get(id = request.POST.get("category"))
			Blog.objects.filter(pk = blog.id).update(title = title, slug = slug, body = body, posted = posted, category = category)
			return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponse('Please make sure all fields are populated')
	else:
		messages.error(request, "Error")
	return render(request, 'blog/index.html', {
		'categories': Category.objects.all(),
        'posts': Blog.objects.all()
		})

	# print(request.title)
	# blog = Blog.objects.get(slug=slug) 
	# print(len(blog.body), 'LENGTH')
	# if len(blog.title) > 0
	pass
