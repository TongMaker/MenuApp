menu = {
    "包饺馍 · Bao y empanadillas": [
        {
            "es": "Rougamo de Cerdo",
            "zh": "肉夹馍",
            "desc": "Hamburguesa estilo Xi’an rellena de cerdo cocido con especias.",
            "price": "6,90 €"
        },
        {
            "es": "Jiaozi fritos / vapor",
            "zh": "煎饺",
            "desc": "Raviolis de cerdo y verduras, fritos o al vapor.",
            "price": "8,90 €"
        },
        {
            "es": "Jiaozi en sopa",
            "zh": "汤水饺",
            "desc": "Jiaozi de carne y verdura en caldo caliente.",
            "price": "9,90 €"
        },
        {
            "es": "Empanadillas fritas",
            "zh": "锅贴",
            "desc": "Empanadillas crujientes por la base al estilo wok.",
            "price": "8,90 €"
        }
    ],

    "面类 · Tallarines": [
        {
            "es": "Tallarines Xi’an",
            "zh": "西安油泼面",
            "desc": "Fideos anchos con chile, cebolleta y vinagre.",
            "price": "8,90 €"
        },
        {
            "es": "Tallarines Zhajiang",
            "zh": "炸酱面",
            "desc": "Fideos con salsa de soja fermentada y cerdo.",
            "price": "9,90 €"
        },
        {
            "es": "Tallarines 2 en 1",
            "zh": "二合一面",
            "desc": "Mezcla Xi’an + Zhajiang.",
            "price": "9,90 €"
        },
        {
            "es": "Tallarines con ternera",
            "zh": "牛肉面",
            "desc": "En caldo casero de ternera.",
            "price": "10,90 €"
        }
    ],

    "饭类 · Arroz": [
        {
            "es": "Arroz tres delicias",
            "zh": "三鲜炒饭",
            "desc": "Arroz con gambas, pollo, cerdo y verduras.",
            "price": "8,90 €"
        },
        {
            "es": "Arroz con ternera",
            "zh": "牛肉盖饭",
            "desc": "Ternera salteada con cebolla y pimientos.",
            "price": "10,90 €"
        },
        {
            "es": "Arroz Kung Pao",
            "zh": "宫保鸡丁饭",
            "desc": "Pollo picante con cacahuetes.",
            "price": "9,90 €"
        }
    ],

    "Bebidas": [
        {"es": "Cerveza Mahou", "zh": "", "desc": "330 ml", "price": "2,80 €"},
        {"es": "Mahou 5 Estrellas", "zh": "", "desc": "330 ml", "price": "3,50 €"},
        {"es": "Coca-Cola", "zh": "", "desc": "330 ml", "price": "3,50 €"},
        {"es": "Agua mineral", "zh": "", "desc": "500 ml", "price": "2,50 €"},
        {"es": "Café", "zh": "", "desc": "Delta", "price": "2,50 €"},
        {"es": "Infusión", "zh": "", "desc": "Té verde", "price": "2,50 €"},
    ]
}

import streamlit as st

st.set_page_config(
    page_title="Gastronomía de Xi'an",
    layout="centered"
)

# --- ESTILOS ---
st.markdown("""
<style>
body {
    background-color: #f5f5f0;
}
.section {
    border-top: 2px solid #b22222;
    border-bottom: 2px solid #b22222;
    padding: 10px 0;
    margin-top: 30px;
}
.item {
    margin-bottom: 14px;
}
.price {
    float: right;
    font-weight: bold;
    color: #b22222;
}
.zh {
    font-size: 1.1em;
    color: #555;
}
.desc {
    font-size: 0.9em;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1 style='text-align:center;color:#b22222;'>Gastronomía de China · Xi’an</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#d4af37;'>西安小吃</h2>", unsafe_allow_html=True)

# --- MENÚ ---
for section, items in menu.items():
    st.markdown(f"<div class='section'><h3>{section}</h3></div>", unsafe_allow_html=True)

    for item in items:
        st.markdown(f"""
        <div class='item'>
            <strong>{item["es"]}</strong>
            <span class='price'>{item["price"]}</span><br>
            <div class='zh'>{item["zh"]}</div>
            <div class='desc'>{item["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)

# --- PIE ---
st.markdown("---")
st.caption(
    "Todos nuestros platos se elaboran con ingredientes frescos. "
    "Algunos pueden contener gluten, frutos secos o marisco."
)
st.caption("¡Gracias por su visita! 🍜")