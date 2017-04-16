from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

def get_prodotto(request, prodotto_id):
    prodotto = Prodotto.objects.get(pk=prodotto_id)
    context = {
        'response': prodotto
    }
    return render(request, 'detail.html', context)


class ProdottoListView(ListView):

    model = Prodotto
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super(ProdottoListView, self).get_context_data(**kwargs)
        return context
