import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("🧮 Aplikasi Turunan Parsial dan Bidang Singgung")

# Input fungsi dari pengguna
x, y = sp.symbols('x y')
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")

try:
    # Menghitung turunan parsial
    f = sp.sympify(fungsi_str)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Tampilkan turunan
    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(fx))
    st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(fy))

    # Input titik evaluasi
    x0 = st.number_input("Nilai x₀:", value=1.0)
    y0 = st.number_input("Nilai y₀:", value=2.0)

    # Hitung nilai fungsi dan gradien di titik (x0, y0)
    f_val = float(f.subs({x: x0, y: y0}))
    fx_val = float(fx.subs({x: x0, y: y0}))
    fy_val = float(fy.subs({x: x0, y: y0}))

    st.write(f"Nilai fungsi di titik ({x0}, {y0}) = ", f_val)
    st.write(f"Gradien di titik ({x0}, {y0}) = ({fx_val}, {fy_val})")

    st.subheader("📈 Grafik Permukaan dan Bidang Singgung")

    # Persiapan data untuk plot
    x_vals = np.linspace(x0 - 2, x0 + 2, 50)
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Evaluasi permukaan fungsi
    Z = sp.lambdify((x, y), f, 'numpy')(X, Y)

    # Persamaan bidang singgung
    Z_tangent = f_val + fx_val * (X - x0) + fy_val * (Y - y0)

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis', label='Permukaan f(x, y)')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red', label='Bidang Singgung')
    ax.set_title("Permukaan f(x, y) dan Bidang Singgungnya")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
