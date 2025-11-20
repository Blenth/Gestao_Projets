from django.shortcuts import render
from django.urls import reverse
def home(request):
    return render(request, 'Cadastro.html')
def Login(request):
    return render(request, 'Login.html')
def List_Product(request):
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
    ]
    html_cards = "<tr>"
    for i, p in enumerate(produtos, start=1):
        url = reverse('ListObject', kwargs={
            'nome': p['nome'],
            'imagem': p['imagem']
        })
        html_cards += f"""
            <td>
                <div class="card">
                    <img src="{p['imagem']}" alt="{p['nome']}">
                    <h3>{p['nome']}</h3>
                    <p>{p['quantidade']} Und</p>
                    <div class="botoes">
                        <button class="info">INFO</button>
                        <button onclick="window.location.href='{url}'" class="controlar">CONTROLAR</button>
                    </div>
                </div>
            </td>
        """
        if i % 5 == 0:
            html_cards += "</tr><tr>"
    html_cards += "</tr>"
    return render(request, 'list.html', {'cards_html': html_cards})
def exibir_produto(request, nome, imagem):
    contexto = {
        'numero_produto': nome,
        'objeto_imagem_url': imagem
    }
    return render(request, 'produto.html', contexto)