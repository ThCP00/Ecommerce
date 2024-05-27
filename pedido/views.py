from django.shortcuts import redirect, render
from produto.models import Produto, Categoria
from .models import Pedido, ItemPedido


def finalizar_pedido(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        erro = request.GET.get('erro')
        total = sum([float(i['preco']) for i in request.session['carrinho']])
        return render(request, 'finalizar_pedido.html', {'carrinho': len(request.session['carrinho']),
                                                        'categorias': categorias,
                                                        'total': total,
                                                        'erro': erro})
    else:
        if len(request.session['carrinho']) > 0:
            x = request.POST
            total = sum([float(i['preco']) for i in request.session['carrinho']])

            carrinho = request.session.get('carrinho')
            listaCarrinho = []
            for i in carrinho:
                listaCarrinho.append({
                    'produto': Produto.objects.filter(id = i['id_produto'])[0],
                    'preco': i['preco'],
                    'quantidade': i['quantidade'],
                })
            

            lambda_func_troco = lambda x: int(x['troco_para'])-total if not x['troco_para'] == '' else ""
            lambda_func_pagamento = lambda x: 'Cartão' if x['meio_pagamento'] == '2' else 'Dinheiro'
            pedido = Pedido(usuario=x['nome'],
                            total = total,
                            troco = lambda_func_troco(x),
                            pagamento = lambda_func_pagamento(x),
                            ponto_referencia = x['pt_referencia'],
                            cep = x['cep'],
                            rua = x['rua'],
                            numero = x['numero'],
                            bairro = x['bairro'],
                            telefone = x['telefone'],
                            )
            pedido.save()
            
            
            ItemPedido.objects.bulk_create(
                ItemPedido(
                    pedido = pedido,
                    produto = v['produto'],
                    quantidade = v['quantidade'],
                    preco = v['preco'],
                ) for v in listaCarrinho
            )
            request.session['carrinho'].clear()
            request.session.save()
            return render(request, 'pedido_finalizado.html') 
        else:
            return redirect('/pedidos/finalizar_pedido?erro=1')