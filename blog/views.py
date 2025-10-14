# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'base.html')

def Login(request):
    return render(request, 'base.html')

def List_Prooduct(request):
    return render(request, 'listProduct.html')  # ou qualquer template que você tenha


def exibir_produto(request, lanche):
    img = Comida(lanche)
    contexto = {
        'numero_produto': lanche,
        'objeto_imagem_url' : img
        }
    return render(request, 'produto.html', contexto)



def Comida(status_code: str) -> str:
    match status_code:
        case "cafe":
            return "https://static.vecteezy.com/ti/fotos-gratis/t2/25282026-estoque-do-misturar-uma-copo-cafe-cafe-com-leite-mais-motivo-topo-visao-comidagrafia-generativo-ai-foto.jpg"
        case "pao":
            return "https://guiadacozinha.com.br/wp-content/uploads/2018/10/paofrancesfolhado.jpg"
        case "suco":
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMFmmPGSvmdIzDXKXhcRcXwgxQTrtju5mo3w&s"
        case "V8":
            return "https://www.motortrend.com/uploads/sites/21/2012/11/1211phr-01-the-biggest-big-block-on-the-planet-1005ci-engine.jpg?w=768&width=768&q=75&format=webp"
        case _:  
            return "Unknown Status"