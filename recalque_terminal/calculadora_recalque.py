
"""Projeto 1 – calculadora_recalque.py (sem Streamlit)"""
import math

G = 9.81
GAMMA = 9810
PI = math.pi

def area(d: float) -> float:
    return PI * (d / 2) ** 2

def vazao(v: float, d: float) -> float:
    return v * area(d)

def perdas_carga(l: float, d: float, q: float, c: float, k: float):
    hf_cont = 10.67 * (l * q ** 1.852) / (c ** 1.852 * d ** 4.87)
    v = q / area(d)
    hf_loc = k * v ** 2 / (2 * G)
    return hf_cont, hf_loc, hf_cont + hf_loc

def altura_manometrica(desnivel: float, hf_total: float) -> float:
    return desnivel + hf_total

def potencia_bomba(q: float, hm: float, eficiencia: float = 1.0):
    p_util = GAMMA * q * hm
    p_hp = p_util / 745.7
    p_req = p_util / eficiencia
    return p_util, p_hp, p_req

def calculo_completo():
    print("== Cálculo Completo de Recalque ==")
    v = float(input("Velocidade (m/s): "))
    d = float(input("Diâmetro (m): "))
    l = float(input("Comprimento (m): "))
    c = float(input("Coef. Hazen-Williams: "))
    k = float(input("Coef. perdas localizadas (K): "))
    z = float(input("Desnível geométrico (m): "))
    eta = float(input("Eficiência da bomba (%): ")) / 100

    q = vazao(v, d)
    hf_cont, hf_loc, hf_tot = perdas_carga(l, d, q, c, k)
    hm = altura_manometrica(z, hf_tot)
    p_util, p_hp, p_req = potencia_bomba(q, hm, eta)

    print(f"Vazão = {q:.4f} m³/s")
    print(f"hf total = {hf_tot:.4f} mca | Altura manométrica = {hm:.2f} mca")
    print(f"Potência útil = {p_util:.2f} W ({p_hp:.2f} HP) | Potência requerida = {p_req:.2f} W")

if __name__ == "__main__":
    calculo_completo()
