from django.http import Http404
from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset =Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

    

   


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()  


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)



class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance
        # return instance


class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

    # try:
    #    Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #    print('no product here')
    #    raise Http404("Product does not exist")
    # except:
    #    print("huh?")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist")


    # print(instance)
    # qs = Product.objects.filter(id=pk)
    # # print(qs)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist")


    context = {
        'object': instance
    }
    return render(request, "products/list.html", context)