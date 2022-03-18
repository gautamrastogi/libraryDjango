from django.shortcuts import render
from .models import Book, Author
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
	books = Book.objects.all()
	authors = Author.objects.all()
	context = {
		"books": books,
		"authors": authors
	}
	return render(request, "homepage.html", context)




class AuthorDetailViewCB(DetailView):
	model = Author
	template_name = "author_detail.html"