from django.shortcuts import render
from pvr.models import Movies
from pvr.forms import Movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     m=Movies.objects.all()
#     return render(request,'index.html',{'m':m})

class movieListview(ListView):
    model=Movies
    template_name="home.html"
    context_object_name="m"

# def addmovie(request):
#     if (request.method == "POST"):
#         m = request.POST['m']
#         d = request.POST['d']
#         i = request.FILES['i']
#         b = Movies.objects.create(movie_name=m,description=d, img=i)
#         b.save()
#         return home(request)
#     return render(request,'addmovies.html')

class createview(CreateView):
    model=Movies
    template_name="addmovies.html"
    fields=['movie_name','description','img']
    success_url=reverse_lazy('pvr:home')

# def viewmovie(request,p):
#     m = Movies.objects.get(id=p)
#     return render(request,'viewmovie.html',{'m':m})

class detailview(DetailView):
    model=Movies
    template_name = "viewmovie.html"
    context_object_name = 'm'

# def deletemovie(request,p):
#
#     m = Movies.objects.get(id=p)
#     m.delete()
#     return home(request)

# def editmovie(request,p):
#     m = Movies.objects.get(id=p)
#     form = Movieform(instance=m)
#     if (request.method == "POST"):
#         form = Movieform(request.POST,request.FILES,instance=m)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'editmovie.html', {'form': form})

class updatemovie(UpdateView):
    model=Movies
    template_name="addmovies.html"
    fields=['movie_name','description','img']
    success_url=reverse_lazy('pvr:home')

class deleteview(DeleteView):
    model=Movies
    template_name='delete.html'
    success_url=reverse_lazy('pvr:home')