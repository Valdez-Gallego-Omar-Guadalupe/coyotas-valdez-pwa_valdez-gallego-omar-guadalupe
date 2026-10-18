from django.shortcuts import render

    # "Base de datos" falsa: una lista de diccionarios en memoria.
    # En un proyecto real esto vendría de un modelo (models.py) y una tabla,
    # pero para ENTENDER qué es SSR no necesitamos base de datos: lo importante
    # es que estos datos se insertan en el HTML *antes* de enviarlo al navegador.
PRODUCTOS =     [
    { "id": 1, "nombre": "Coyota de piloncillo", "categoria": "Coyotas", "precio": 18, "stock": 50, "imagen": "img/coyota-piloncillo.svg" },
    { "id": 2, "nombre": "Coyota de jamoncillo", "categoria": "Coyotas", "precio": 20, "stock": 40, "imagen": "img/coyota-jamoncillo.svg" },
    { "id": 3, "nombre": "Coyota de guayaba", "categoria": "Coyotas", "precio": 20, "stock": 40, "imagen": "img/coyota-guayaba.svg" },
    { "id": 4, "nombre": "Coyota de cajeta", "categoria": "Coyotas", "precio": 22, "stock": 35, "imagen": "img/coyota-cajeta.svg" },
    { "id": 5, "nombre": "Caja de 12 coyotas", "categoria": "Coyotas", "precio": 200, "stock": 15, "imagen": "img/caja-12-coyotas.svg" },
    { "id": 6, "nombre": "Empanada de calabaza", "categoria": "Pan tradicional", "precio": 20, "stock": 30, "imagen": "img/empanada-calabaza.svg" },
    { "id": 7, "nombre": "Pan de mujer", "categoria": "Pan tradicional", "precio": 18, "stock": 30, "imagen": "img/pan-de-mujer.svg" },
    { "id": 8, "nombre": "Galleta de manteca", "categoria": "Pan tradicional", "precio": 15, "stock": 60, "imagen": "img/galleta-manteca.svg" },
    { "id": 9, "nombre": "Bizcocho", "categoria": "Pan tradicional", "precio": 15, "stock": 40, "imagen": "img/bizcocho.svg" },
    { "id": 10, "nombre": "Pan de elote", "categoria": "Pan tradicional", "precio": 40, "stock": 20, "imagen": "img/pan-de-elote.svg" },
    { "id": 11, "nombre": "Café de olla", "categoria": "Bebidas", "precio": 30, "stock": 50, "imagen": "img/cafe-de-olla.svg" },
    { "id": 12, "nombre": "Champurrado", "categoria": "Bebidas", "precio": 35, "stock": 30, "imagen": "img/champurrado.svg" },
    { "id": 13, "nombre": "Chocolate caliente", "categoria": "Bebidas", "precio": 35, "stock": 30, "imagen": "img/chocolate-caliente.svg" },
    { "id": 14, "nombre": "Atole de pinole", "categoria": "Bebidas", "precio": 30, "stock": 30, "imagen": "img/atole-pinole.svg" },
    { "id": 15, "nombre": "Vaso de leche", "categoria": "Bebidas", "precio": 20, "stock": 40, "imagen": "img/vaso-de-leche.svg" }
    ]


def vista_ssr(request):
        """
        Vista con Renderizado en Servidor (SSR).

        request: el objeto que representa la petición que hizo el navegador.

        render() hace tres cosas:
        1) toma la plantilla 'catalogo/catalogo_ssr.html'
        2) le inyecta el diccionario de "contexto" (aquí: la lista de productos)
        3) devuelve el HTML final, YA CON LOS DATOS DENTRO, listo para el navegador.

        Por eso es "servidor": el HTML que llega al navegador ya trae escritos
        los nombres y precios. Si haces clic derecho > "Ver código fuente de la
        página" verás los productos en el HTML, aunque JavaScript esté desactivado.
        Compáralo con la vista CSR de la Parte B, donde el HTML llega vacío y es
        JavaScript quien dibuja los productos DESPUÉS, ya en el navegador.
        """
        contexto = {"productos": PRODUCTOS}
        return render(request, 'catalogo/catalogo_ssr.html', contexto)