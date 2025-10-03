#TiendaVirtual.py
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Tienda Virtual", page_icon="🛒", layout="wide")

st.title("🏪 Tienda Virtual")
st.write("Bienvenido, selecciona productos y simula tu compra.")

# Catálogo de productos con imágenes
productos = {
    1: {
        "nombre": "Laptop",
        "precio": 2500.00,
        "imagen": "https://www.pcfactory.com.pe/public/foto/3576/1_1000.jpg"  # ejemplo
    },
    2: {
        "nombre": "Mouse Gamer",
        "precio": 120.00,
        "imagen": "https://www.pcfactory.com.pe/public/foto/2339/1_1000.jpg?t=1738875755119"
    },
    3: {
        "nombre": "Teclado Mecánico",
        "precio": 350.00,
        "imagen": "https://www.pcfactory.com.pe/public/foto/1415/1_1000.jpg?t=1729699181605"
    },
}

# Carrito
if "carrito" not in st.session_state:
    st.session_state["carrito"] = {}

# Mostrar productos en columnas
st.subheader("📦 Catálogo")
cols = st.columns(3)

for idx, (pid, info) in enumerate(productos.items()):
    with cols[idx % 3]:
        st.image(info["imagen"], width=200)
        st.write(f"**{info['nombre']}**")
        st.write(f"💵 Precio: S/. {info['precio']:.2f}")
        if st.button(f"Agregar {info['nombre']}", key=pid):
            st.session_state["carrito"][pid] = st.session_state["carrito"].get(pid, 0) + 1
            st.success(f"{info['nombre']} agregado al carrito")

# Mostrar carrito
st.subheader("🛒 Carrito de Compras")
if not st.session_state["carrito"]:
    st.info("El carrito está vacío.")
else:
    total = 0
    for pid, cantidad in st.session_state["carrito"].items():
        prod = productos[pid]
        subtotal = prod["precio"] * cantidad
        total += subtotal
        st.write(f"➡️ {prod['nombre']} x {cantidad} = S/. {subtotal:.2f}")
    st.success(f"💰 TOTAL = S/. {total:.2f}")

    if st.button("✅ Finalizar compra"):
        st.session_state["carrito"].clear()
        st.success("¡Gracias por tu compra! 🎉")
