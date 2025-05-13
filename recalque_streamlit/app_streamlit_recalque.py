
import streamlit as st
import math

G = 9.81
GAMMA = 9810
PI = math.pi

def area(d):
    return PI * (d / 2) ** 2

def vazao(v, d):
    return v * area(d)

def perdas_carga(l, d, q, c, k):
    hf_cont = 10.67 * (l * q ** 1.852) / (c ** 1.852 * d ** 4.87)
    v = q / area(d)
    hf_loc = k * v ** 2 / (2 * G)
    return hf_cont, hf_loc, hf_cont + hf_loc

def altura_manometrica(z, hf):
    return z + hf

def potencia(q, h, eta):
    p_util = GAMMA * q * h
    p_hp = p_util / 745.7
    p_req = p_util / eta
    return p_util, p_hp, p_req

st.set_page_config(page_title="Calculadora Recalque", page_icon="💧")
st.title("💧 Calculadora Completa de Recalque")

menu = st.selectbox("Escolha o tipo de cálculo:", [
    "Cálculo Completo", "Vazão", "Perda de carga", "Altura manométrica", "Potência da bomba"
])

if menu == "Cálculo Completo":
    v = st.number_input("Velocidade (m/s)", step=0.1)
    d = st.number_input("Diâmetro (m)", step=0.01)
    l = st.number_input("Comprimento (m)", step=1.0)
    c = st.number_input("Coef. Hazen-Williams", step=1.0)
    k = st.number_input("Perda localizada (K)", step=0.1)
    z = st.number_input("Desnível geométrico (m)")
    eta = st.number_input("Eficiência (%)", value=70.0) / 100
    if st.button("Calcular tudo"):
        q = vazao(v, d)
        hf_cont, hf_loc, hf_tot = perdas_carga(l, d, q, c, k)
        hm = altura_manometrica(z, hf_tot)
        p_util, p_hp, p_req = potencia(q, hm, eta)
        st.success(f"""Vazão = {q:.4f} m³/s
hf total = {hf_tot:.4f} mca
Altura manométrica = {hm:.2f} mca
Potência útil = {p_util:.2f} W ({p_hp:.2f} HP)
Potência requerida = {p_req:.2f} W""")

elif menu == "Vazão":
    v = st.number_input("Velocidade (m/s)", step=0.1)
    d = st.number_input("Diâmetro (m)", step=0.01)
    if st.button("Calcular vazão"):
        q = vazao(v, d)
        st.success(f"Vazão = {q:.4f} m³/s")

elif menu == "Perda de carga":
    l = st.number_input("Comprimento (m)", step=1.0)
    d = st.number_input("Diâmetro (m)", step=0.01)
    q = st.number_input("Vazão (m³/s)", step=0.001)
    c = st.number_input("Coef. Hazen-Williams", step=1.0)
    k = st.number_input("K total", step=0.1)
    if st.button("Calcular perdas"):
        hf_cont, hf_loc, hf_tot = perdas_carga(l, d, q, c, k)
        st.success(f"hf contínua = {hf_cont:.4f} | hf localizada = {hf_loc:.4f} | hf total = {hf_tot:.4f} mca")

elif menu == "Altura manométrica":
    z = st.number_input("Desnível geométrico (m)")
    hf = st.number_input("hf total (mca)")
    if st.button("Calcular altura manométrica"):
        h = altura_manometrica(z, hf)
        st.success(f"Altura manométrica = {h:.2f} mca")

elif menu == "Potência da bomba":
    q = st.number_input("Vazão (m³/s)", step=0.001)
    h = st.number_input("Altura manométrica (m)")
    eta = st.number_input("Eficiência (%)", value=70.0) / 100
    if st.button("Calcular potência"):
        p_util, p_hp, p_req = potencia(q, h, eta)
        st.success(f"Potência útil = {p_util:.2f} W ({p_hp:.2f} HP) | Potência requerida = {p_req:.2f} W")
