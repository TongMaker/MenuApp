import streamlit as st
import os

# ======================
# CONFIGURACIÓN PÁGINA
# ======================
st.set_page_config(
    page_title="Gastronomía de Xi’an",
    page_icon="🍜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# CABECERA
# ======================
st.title("🍜 Gastronomía de Xi’an")
st.caption("西安小吃 · Cocina tradicional de Shaanxi")
st.markdown("---")

# ======================
# FUNCIÓN PLATO
# ======================
def plato(nombre_es, nombre_zh, descripcion, precio, imagen):
    titulo = f"{nombre_zh} · {nombre_es}" if nombre_zh else nombre_es
    with st.expander(f"**{titulo}** — {precio}"):
        if os.path.exists(imagen):
            st.image(imagen, use_container_width=True)
        else:
            st.info("📷 Imagen próximamente")
        st.write(descripcion)

# ======================
# DATOS MENÚ
# ======================
menu = {
    "🥟 包饺馍 · Bao y empanadillas": [
        {
            "es": "Rougamo de Cerdo",
            "zh": "肉夹馍",
            "desc": "Hamburguesa estilo Xi’an rellena de cerdo cocido con especias.",
            "price": "6,90 €",
            "img": "images/肉夹馍.jpg"
        },
        {
            "es": "Jiaozi fritos / vapor",
            "zh": "煎饺",
            "desc": "Raviolis de cerdo y verduras, fritos o al vapor.",
            "price": "8,90 €",
            "img": "images/煎饺.jpg"
        },
        {
            "es": "Jiaozi en sopa",
            "zh": "汤水饺",
            "desc": "Jiaozi de carne y verdura en caldo caliente.",
            "price": "9,90 €",
            "img": "images/汤水饺.jpg"
        },
        {
            "es": "Empanadillas fritas",
            "zh": "锅贴",
            "desc": "Empanadillas crujientes por la base al estilo wok.",
            "price": "8,90 €",
            "img": "images/锅贴.jpg"
        }
    ],

    "🍜 面类 · Tallarines": [
        {
            "es": "Tallarines Xi’an",
            "zh": "西安油泼面",
            "desc": "Fideos anchos con chile, cebolleta y vinagre.",
            "price": "8,90 €",
            "img": "images/西安油泼面.jpg"
        },
        {
            "es": "Tallarines Zhajiang",
            "zh": "炸酱面",
            "desc": "Fideos con salsa de soja fermentada y cerdo.",
            "price": "9,90 €",
            "img": "images/炸酱面.jpg"
        },
        {
            "es": "Tallarines 2 en 1",
            "zh": "二合一面",
            "desc": "Mezcla Xi’an + Zhajiang.",
            "price": "9,90 €",
            "img": "images/二合一面.jpg"
        },
        {
            "es": "Tallarines con ternera",
            "zh": "牛肉面",
            "desc": "En caldo casero de ternera.",
            "price": "10,90 €",
            "img": "images/牛肉面.jpg"
        }
    ],

    "🍚 饭类 · Arroz": [
        {
            "es": "Arroz tres delicias",
            "zh": "三鲜炒饭",
            "desc": "Arroz con gambas, pollo, cerdo y verduras.",
            "price": "8,90 €",
            "img": "images/三鲜炒饭.jpg"
        },
        {
            "es": "Arroz con ternera",
            "zh": "牛肉盖饭",
            "desc": "Ternera salteada con cebolla y pimientos.",
            "price": "10,90 €",
            "img": "images/牛肉盖饭.jpg"
        },
        {
            "es": "Arroz Kung Pao",
            "zh": "宫保鸡丁饭",
            "desc": "Pollo picante con cacahuetes.",
            "price": "9,90 €",
            "img": "images/宫保鸡丁饭.jpg"
        }
    ],

    "🥤 Bebidas": [
        {"es": "Cerveza Mahou", "zh": "", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Mahou 5 Estrellas", "zh": "", "desc": "330 ml", "price": "3,50 €", "img": ""},
        {"es": "Coca-Cola", "zh": "", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Agua mineral", "zh": "", "desc": "500 ml", "price": "2,50 €", "img": ""},
        {"es": "Café", "zh": "", "desc": "Delta", "price": "1,80 €", "img": ""},
        {"es": "Infusión", "zh": "", "desc": "Té verde", "price": "1,80 €", "img": ""}
    ]
}

# ======================
# RENDER MENÚ
# ======================
for seccion, platos in menu.items():
    st.subheader(seccion)
    for p in platos:
        plato(
            p["es"],
            p["zh"],
            p["desc"],
            p["price"],
            p["img"]
        )

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption(
    "ℹ️ Algunos platos pueden contener gluten, frutos secos o marisco.\n\n"
    "📱 Menú digital · Escanee el QR · Xi’an"
)
