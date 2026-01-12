from django.urls import path
from pedido import views

app_name = "pedido"

urlpatterns = [
    path("pagar/", views.Pagar.as_view(), name="pagar"),
    path("fechar-pedido/", views.FecharPedido.as_view(), name="fecharpedido"),
    path("detalhe-pedido/", views.DetalhePedido.as_view(), name="detalhepedido"),
]
