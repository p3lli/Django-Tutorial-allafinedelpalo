from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.forms import ModelForm
from ecommerce.models import Casa, Prodotto
import logging

logger = logging.getLogger('textlogger')

def index(request):
    case_produttrici = Casa.objects.all().values_list('nome', flat=True)
    return render(
        request,
        'index.html',
        context={'case_produttrici': case_produttrici},
    )

def contacts(request):
    return render(
        request,
        'contacts.html',
        context={},
    )

def product_show(request, product_id):
    prodotto = Prodotto.objects.get(pk=product_id)
    logger.info(''.join(['showing ', prodotto.nome]))
    context = {
        'response': prodotto
    }
    return render(request, 'detail.html', context)

class ProductForm(ModelForm):
    class Meta:
        model = Prodotto
        fields = ['nome', 'dettagli', 'prezzo', 'casa']

class ProductListView(ListView):

    model = Prodotto
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context

@csrf_exempt
@login_required
def product_create(request, template_name='product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info(''.join([form.cleaned_data['nome'],
                             ' has been inserted']))
        return redirect('products')
    return render(request, template_name, {'form':form})

@csrf_exempt
@login_required
def product_update(request, product_id, template_name='product_form.html'):
    product = get_object_or_404(Prodotto, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        logger.info(''.join([form.cleaned_data['nome'],
                             ' has been modified']))
        return redirect('products')
    return render(request, template_name, {'form':form})

@csrf_exempt
@login_required
def product_delete(request, product_id, template_name='product_confirm_delete.html'):
    product = get_object_or_404(Prodotto, pk=product_id)
    if request.method=='POST':
        product.delete()
        logger.info(''.join([product.nome, ' has been deleted']))
        return redirect('products')
    return render(request, template_name, {'object':product})
