// csr.js — Renderizado en el Cliente (CSR)
// "CSR" significa que el HTML llega casi vacío y es ESTE archivo JavaScript,
// ya corriendo en el navegador del usuario, quien construye el contenido.

// 1) Buscamos el contenedor vacío que dejamos en index.html
const contenedorCatalogo = document.getElementById("catalogo");

// Guarda todos los productos en memoria: así filtrarCatalogo() no repite
// el fetch cada vez, solo rellee el grid con el subconjunto pedido.
let todosLosProductos = [];

// Dibuja en el grid solo los productos de la categoría indicada.
// Si categoria === "Todos", dibuja el catálogo completo.
function filtrarCatalogo(categoria) {
  const visibles =
    categoria === "Todos"
      ? todosLosProductos
      : todosLosProductos.filter((p) => p.categoria === categoria);

  contenedorCatalogo.innerHTML = "";

  if (visibles.length === 0) {
    contenedorCatalogo.innerHTML = "<p>No hay productos en esta categoría.</p>";
    return;
  }

  visibles.forEach((producto) => {
    const tarjeta = document.createElement("div");
    tarjeta.className = "producto";

    tarjeta.innerHTML = `
      <img class="producto__foto" src="${producto.imagen}" alt="${producto.nombre}" loading="lazy">
      <strong>${producto.nombre}</strong>
      <span class="precio">$${producto.precio}</span>
      <p>Stock: ${producto.stock}</p>
      <button type="button" data-id="${producto.id}">Agregar al carrito</button>
    `;

    contenedorCatalogo.appendChild(tarjeta);

    // conectamos el botón recién creado con la función agregarAlCarrito() de carrito.js
    tarjeta.querySelector("button").addEventListener("click", () => {
      agregarAlCarrito(producto);
    });
  });
}

// Activa el botón de filtro presionado y desactiva los demás.
// Separa "quién está activo" de "qué productos se muestran",
// por eso es una función propia.
function activarFiltro(botonPresionado) {
  document.querySelectorAll(".filtro").forEach((btn) => {
    btn.classList.toggle("filtro--activo", btn === botonPresionado);
  });
}

// 2) fetch() le pide el archivo catalogo.json al servidor (aquí simula una API real).
//    fetch() devuelve una "promesa": un valor que llegará más adelante, no de inmediato.
fetch("catalogo.json")
  .then((respuesta) => respuesta.json()) // convierte el texto recibido en un array de objetos JS
  .then((productos) => {
    // 3) Guardamos todos los productos y borramos las tarjetas esqueleto
    todosLosProductos = productos;
    contenedorCatalogo.removeAttribute("aria-busy");
    contenedorCatalogo.removeAttribute("aria-label");

    // Dibujamos el catálogo completo al inicio
    filtrarCatalogo("Todos");

    // 4) Escuchamos los clics en los botones de filtro
    document.querySelectorAll(".filtro").forEach((btn) => {
      btn.addEventListener("click", () => {
        activarFiltro(btn);
        filtrarCatalogo(btn.dataset.categoria);
      });
    });
  })
  .catch((error) => {
    // si algo falla (por ejemplo, sin conexión y sin caché), avisamos en pantalla
    contenedorCatalogo.innerHTML = "<p>No se pudo cargar el catálogo. Intenta más tarde.</p>";
    contenedorCatalogo.removeAttribute("aria-busy");
    contenedorCatalogo.removeAttribute("aria-label");
    console.error("Error al cargar catálogo:", error);
  });
