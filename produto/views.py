from django.shortcuts import render, redirect
from .models import Produto, Categoria
# Create your views here.

def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,
                                        })

def categorias(request, id):
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'produtos': produtos,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,})

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto, 
                                            'carrinho': len(request.session['carrinho']),
                                            'categorias': categorias,
                                            'erro': erro})

def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)

    def removeLixo(adicional):
        adicionais = x.copy()
        adicionais.pop('id')
        adicionais.pop('csrfmiddlewaretoken')
        adicionais.pop('quantidade')
        adicionais = list(adicionais.items())

        return adicionais
        
    adicionais = removeLixo(x)    


    id = int(x['id'][0])
    preco_total = Produto.objects.filter(id=id)[0].preco

    
    preco_total *= int(x['quantidade'][0])
    data = {'id_produto': int(x['id'][0]),
            'preco': preco_total,
            'adicionais': adicionais,
            'quantidade': x['quantidade'][0]}

    request.session['carrinho'].append(data)
    request.session.save()
    #return HttpResponse(request.session['carrinho'])
    return redirect(f'/ver_carrinho')

def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_motrar = []
    for i in request.session['carrinho']:
        prod = Produto.objects.filter(id=i['id_produto'])
        dados_motrar.append(
            {'imagem': prod[0].img.url,
             'nome': prod[0].nome_produto,
             'quantidade': i['quantidade'],
             'preco': i['preco'],
             'id': i['id_produto']
             }
        )
    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'carrinho.html', {'dados': dados_motrar,
                                             'total': total,
                                             'carrinho': len(request.session['carrinho']),
                                             'categorias': categorias,
                                             })

def remover_carrinho(request, id):
    request.session['carrinho'].pop(id)
    request.session.save()
    return redirect('/ver_carrinho')


