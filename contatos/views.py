from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    # fazer paginação
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    # quando o contaqto for desativado ele não poder ser acessador via browser
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    # identificador da pesquisa
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo pesquisa não pode ficar vazio.'
        )
        return redirect('index')

    if not termo:
        messages.add_message(
            request,
            messages.INFO,
            'Contato Não Localizado.'
        )

    if termo:
        messages.add_message(
            request,
            messages.SUCCESS,
            'Contato Localizado.'
        )




    campos = Concat('nome', Value(' '), 'sobrenome')  # pesquisa com nome e sobrenome
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    '''
        #pesquisa simplificada
        contatos = Contato.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )'''
    # fazer paginação
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
