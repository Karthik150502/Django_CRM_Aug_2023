from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from card_app.models import Company, Products
from django.urls import reverse_lazy





# Create your views here.


# def index(request):
#     return render(request, "index.html")



# class Myclass(View):
#     def get(self, request):
#         return HttpResponse("This message is generated with the help of the class based Views, 'CBV'!!")
    

class Myclass(TemplateView):
    template_name = "index.html"
    




# def new(request):
#     res = Company.objects.all
#     return render(request, "index.html", {'result':res})


# or 


class CompanyList(ListView):
    context_object_name = "company_detail"
    model = Company
    


class CompanyDetailView(DetailView):
    context_object_name = "company_detail"
    model = Company



class CompanyCreateView(CreateView):
    fields = [
        'name',
        'ceo',
        'origin'
    ]
    model = Company


class CompanyUpdateView(UpdateView):
    fields = [
        "name",
        "ceo",        
    ]
    model = Company

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy("card_app:list")
    context_object_name = "company_detail"
    

class ProductsUpdateView(UpdateView):
    fields = [
        "product_name",
        "mileage",
        "cc",
        "price",
        "color"
    ]
    model = Products
    context_object_name = "products_detail"
    # companyid=.kwargs['pk']
    success_url = reverse_lazy("card_app:list")

class ProductsCreateView(CreateView):
    # fields = [
    #     "product_name",
    #     "mileage",
    #     "cc",
    #     "price",
    #     "color",
    #     "year",
    #     "company"
    # ]
    # success_url = reverse_lazy("card_app:list")
    fields = "__all__"
    model = Products
    success_url = reverse_lazy("card_app:list")

class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy("card_app:list")
    context_object_name = "products_detail"


class ProductDetailView(DetailView):
    context_object_name = "products_detail"
    success_url = reverse_lazy("card_app:list")
    model = Products



'''

    product_name = models.CharField(max_length = 200)
    mileage = models.IntegerField()
    cc = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length = 200)
    year = models.IntegerField()
    company = models.ForeignKey(Company, related_name = "companies", on_delete = models.CASCADE)


'''