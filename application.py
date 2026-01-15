import streamlit as st
import os


# 隐藏右下角的 "Hosted with Streamlit" 水印（包括红皇冠）
st.markdown("""
    <style>
    /* 隐藏整个 footer 区域 */
    footer {
        visibility: hidden;
    }
    /* 如果 footer 被隐藏后留白，可以进一步压缩底部空间 */
    .stApp {
        padding-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)







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
        {"es": "Rougamo de Cerdo", "zh": "肉夹馍", "desc": "Hamburguesa estilo Xi’an rellena de cerdo cocido con especias.", "price": "5,85 €", "img": "images/肉夹馍.jpg"},
        {"es": "Jiaozi fritas", "zh": "煎饺", "desc": "Raviolis de cerdo y verduras, fritos o al vapor.", "price": "6,95 €", "img": "images/煎饺.jpg"},
        {"es": "Jiaozi en sopa", "zh": "汤水饺", "desc": "Jiaozi de carne y verdura en caldo caliente.", "price": "8,50 €", "img": "images/汤水饺.jpg"},
        {"es": "Empanadillas fritas", "zh": "锅贴", "desc": "Empanadillas crujientes por la base al estilo wok.", "price": "6,95 €", "img": "images/锅贴.jpg"},
        {"es": "Rollito de primavera frita", "zh": "炸春卷", "desc": "Rollito crujientes de verdura.", "price": "6,95 €", "img": "images/春卷.jpg"},
        {"es": "Pao mo", "zh": "西安泡馍", "desc": "sopa tradicional de pan desmenuzado con ternera estilo Xian", "price": "12,95 €", "img": "images/西安泡馍.jpg"}
    ],
    "🍜 面类 · Tallarines": [
        {"es": "Tallarines Xi’an", "zh": "西安油泼面", "desc": "Fideos anchos con chile, cebolleta y vinagre.", "price": "8,00 €", "img": "images/西安油泼面.jpg"},
        {"es": "Tallarines Zhajiang", "zh": "炸酱面", "desc": "Fideos con salsa de soja fermentada y cerdo.", "price": "8,50 €", "img": "images/炸酱面.jpg"},
        {"es": "Tallarines 2 en 1", "zh": "二合一面", "desc": "Mezcla Xi’an + Zhajiang.", "price": "9,50 €", "img": "images/二合一面.jpg"},
        {"es": "Tallarines con ternera", "zh": "牛肉面", "desc": "En caldo casero de ternera.", "price": "9,85 €", "img": "images/牛肉面.jpg"},
        {"es": "Tallarines salteado con ternera", "zh": "牛肉炒面", "desc": "Tallarines salteado con ternera.", "price": "8,50 €", "img": "images/牛肉炒面.jpg"},
        {"es": "Tallarines salteado con verdura", "zh": "素炒面", "desc": "Tallarines salteado con verdura y huevo.", "price": "7,50 €", "img": "images/素炒面.jpg"}
    ],
    "🍚 饭类 · Arroz": [
        {"es": "Arroz tres delicias", "zh": "三鲜炒饭", "desc": "Arroz frito.", "price": "7,50 €", "img": "images/三鲜炒饭.jpg"},
        {"es": "Arroz tres delicias con gamba", "zh": "三鲜虾仁炒饭", "desc": "Arroz frito.", "price": "8,80 €", "img": "images/三鲜虾仁炒饭.jpg"},
        {"es": "Arroz con ternera", "zh": "牛肉盖饭", "desc": "Ternera salteada con cebolla y pimientos.", "price": "9,90 €", "img": "images/牛肉盖饭.jpg"},
        {"es": "Arroz Kung Pao", "zh": "宫保鸡丁饭", "desc": "Pollo picante con cacahuetes.", "price": "8,50 €", "img": "images/宫保鸡丁饭.jpg"},
        {"es": "Arroz bolas carne agridulce", "zh": "糖醋鸡丸饭", "desc": "bolas de carne de pollo a la salsa agridulce.", "price": "8,50 €", "img": "images/糖醋鸡丸饭.jpg"},
        {"es": "Arroz blanco", "zh": "米饭", "desc": "Arroz blanco al vapor.", "price": "3,00 €", "img": "images/米饭.jpg"}
    ],
    "🍚 小菜 · Aperitivos": [
        {"es": "Estofado racion pequeño(ternera, patita de pollo, callos)", "zh": "小份卤煮(牛肉, 鸡爪, 牛肚)", "desc": "Estofado chino en salsa de soja racion pequeño.", "price": "3,80 €", "img": "images/小份卤煮.jpg"},
        {"es": "Ternera estofado", "zh": "卤牛肉", "desc": "Ternera estofada chino en salsa de soja racion grande.", "price": "12,50 €", "img": "images/卤牛肉.jpg"},
        {"es": "platito aperitivo", "zh": "小凉菜", "desc": "Aperitivo verdura.", "price": "2,50 €", "img": "images/小凉菜.jpg"}
    ],
    "🥤 Bebidas": [
        {"es": "Cerveza Mahou grifo", "zh": "mahou啤酒管", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Mahou 5 Estrellas", "zh": "mahou五星啤酒", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Mahou sin alcohol", "zh": "无酒精啤酒", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Cerveza tshindao", "zh": "青岛啤酒", "desc": "330 ml", "price": "3,50 €", "img": ""},
        {"es": "Coca-Cola", "zh": "可口可乐", "desc": "330 ml", "price": "2,80 €", "img": ""},
        {"es": "Agua mineral", "zh": "矿泉水", "desc": "500 ml", "price": "2,50 €", "img": ""},
        {"es": "Café", "zh": "咖啡", "desc": "Delta", "price": "1,80 €", "img": ""},
        {"es": "Infusión", "zh": "茶", "desc": "Té verde", "price": "1,80 €", "img": ""},
        {"es": "Te chino", "zh": "中国茶", "desc": "Té verde", "price": "2,80 €", "img": ""}
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
