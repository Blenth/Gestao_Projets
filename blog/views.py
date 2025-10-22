# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


produtos = [
        {
            "nome": "café",
            "quantidade": 30,
            "imagem": "https://s2-g1.glbimg.com/cSwyuz3Gg0t6TBKAHzkq68v81r4=/0x0:4479x2686/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2025/A/0/8Tz12FRCKuANsWHn0bYQ/adobestock-1210523825-1-.jpeg"
        },
        {
            "nome": "Leite",
            "quantidade": 12,
            "imagem": "https://img.freepik.com/fotos-gratis/um-copo-de-leite-fresco-em-um-fundo-de-madeira_144627-13448.jpg"
        },
        {
            "nome": "Açúcar",
            "quantidade": 25,
            "imagem": "https://img.freepik.com/fotos-premium/acucar-em-po-em-colher-de-madeira-e-tigela_88281-3202.jpg"
        },
    ]


def home(request):
    return render(request, 'Cadastro.html')

def Login(request):
    return render(request, 'Login.html')

def List_Prooduct(request):
    produtos = [
        {
            "nome": "Café",
            "quantidade": 30,
            "imagem": "https://s2-g1.glbimg.com/cSwyuz3Gg0t6TBKAHzkq68v81r4=/0x0:4479x2686/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2025/A/0/8Tz12FRCKuANsWHn0bYQ/adobestock-1210523825-1-.jpeg"
        },
        {
            "nome": "Leite",
            "quantidade": 12,
            "imagem": "https://img.freepik.com/fotos-gratis/um-copo-de-leite-fresco-em-um-fundo-de-madeira_144627-13448.jpg"
        },
        {
            "nome": "Açúcar",
            "quantidade": 25,
            "imagem": "https://img.freepik.com/fotos-premium/acucar-em-po-em-colher-de-madeira-e-tigela_88281-3202.jpg"
        },
        {
            "nome": "Biscoito",
            "quantidade": 10,
            "imagem": "https://img.freepik.com/fotos-gratis/deliciosos-biscoitos-caseiros_144627-17879.jpg"
        },
        {
            "nome": "Arroz",
            "quantidade": 50,
            "imagem": "https://img.freepik.com/fotos-gratis/arroz-cru-em-tigela-de-madeira_1150-37517.jpg"
        },
        {
            "nome": "Feijão",
            "quantidade": 20,
            "imagem": "https://img.freepik.com/fotos-gratis/feijao-preto-cru-em-tigela-de-madeira_1150-37522.jpg"
        },
    ]

    html_cards = "<tr>"
    for i, p in enumerate(produtos, start=1):
        html_cards += f"""
        <td>
          <div class="card">
            <img src="{p['imagem']}" alt="{p['nome']}">
            <h3>{p['nome']}</h3>
            <p>{p['quantidade']} Und</p>
            <div class="botoes">
              <button class="info">INFO</button>
              <button class="controlar">CONTROLAR</button>
            </div>
          </div>
        </td>
        """
        if i % 5 == 0 and i < len(produtos):
            html_cards += "</tr><tr>"

    html_cards += "</tr>"

    return render(request, 'List.html', {'cards_html': html_cards})

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