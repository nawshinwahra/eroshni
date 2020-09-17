from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm, LoginForm,RegisterForm

def home_page(request):
	context = {
	"title":"Hello world!",
	"content": "Welcome to Home page.",

	}
	if request.user.is_authenticated():
		context["premium_content"] = "YEAHHHH"
	return render(request, "home_page.html",context)

def about_page(request):
	context = {
	"title":"About Page",
	"content": "Welcome to About page."
	}
	return render(request, "home_page.html",context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title":"Contact Page",
	"content": "Welcome to Contact page.",
	"form":contact_form,
	}
	if contact_form.is_valid():
	   print(contact_form.cleaned_data)
	#if request.method == "POST":
	#print(request.POST)
	#print(request.POST.get('fullname'))
	#print(request.POST.get('email'))
	#print(request.POST.get('content'))
	return render(request, "contact/view.html",context)


def login_page(request):
	form = LoginForm(request.POST or None)
	context ={
	 "form":form
	}
	print("user loged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(user)
		#print(request.user.is_authenticated())
		if user is not None:
			print(request.user.is_authenticated())
			login(request, user)
			#Redirect to a success page.
			#context['form'] = LoginForm()
			return redirect("/")
		else:
			#return an 'invalid login' error message.
			print("Error")

	return render(request, "auth/login.html",context)


User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context ={
	 "form":form
	}
	if form.is_valid():
	   print(form.cleaned_data)
	   username = form.cleaned_data.get("username")
	   email = form.cleaned_data.get("email")
	   password = form.cleaned_data.get("password")
	   new_user = User.objects.create_user(username, email, password)
	   print(new_user)
	   
	return render(request, "auth/register.html", context)




def home_page_old(request):
	html_ = """
<!doctype html>
<html lang="en">
	<head>
	<!-- Required meta tags -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

	<title>Hello, world!</title>
	</head>
	<body>
	<div class='text-center'>
	<h1>Hello, world!</h1>
	</div>

	<!-- Optional JavaScript -->
	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	</body>
 </html>
	"""
	return HttpResponse(html_)