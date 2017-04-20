from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.forms import ModelForm
from ecommerce.models import Casa, Prodotto

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

def prodotto_show(request, prodotto_id):
    prodotto = Prodotto.objects.get(pk=prodotto_id)
    context = {
        'response': prodotto
    }
    return render(request, 'detail.html', context)

class ProdottoForm(ModelForm):
    class Meta:
        model = Prodotto
        fields = ['nome', 'dettagli', 'prezzo', 'casa']

class ProdottoListView(ListView):

    model = Prodotto
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super(ProdottoListView, self).get_context_data(**kwargs)
        return context

@csrf_exempt
def prodotto_create(request, template_name='product_form.html'):
    form = ProdottoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form':form})

@csrf_exempt
def prodotto_update(request, prodotto_id, template_name='product_form.html'):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)
    form = ProdottoForm(request.POST or None, instance=prodotto)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form':form})

@csrf_exempt
def prodotto_delete(request, prodotto_id, template_name='product_confirm_delete.html'):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)
    if request.method=='POST':
        prodotto.delete()
        return redirect('products')
    return render(request, template_name, {'object':prodotto})
