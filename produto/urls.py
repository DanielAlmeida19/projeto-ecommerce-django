from django.urls import path

from produto import views

app_name = "produto"

urlpatterns = [
    path("", views.ListaProdutos.as_view(), name="lista"),
    path("<slug>", views.DetalheProduto.as_view(), name="detalhe"),
    path("adicionar-ao-carrinho/", views.AdicionarAoCarrinho.as_view(), name="adicionaraocarrinho"),
    path("remover-do-carrinho/", views.RemoverDoCarrinho.as_view(), name="removerdocarrinho"),
    path("carrinho/", views.Carrinho.as_view(), name="carrinho"),
    path("finalizar/", views.Finalizar.as_view(), name="finalizar"),
]
