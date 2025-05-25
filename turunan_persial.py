import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("📊 Aplikasi Turunan Parsial dan Visualisasi 3D")
st.subheader("Kasus: Model Biaya Produksi (Ekonomi)")

# Input simbolik
x, y = sp.symbols('x y')
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "100*x + 80*y + 10*x**2 + 5*y**2")

try:
    f = sp.sympify(fungsi_str)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.latex(r"f(x, y) = " + sp.latex(f))
    st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(fx))
    st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(fy))

    # Titik evaluasi
    x0 = st.number_input("Nilai x₀:", value=2.0)
    y0 = st.number_input("Nilai y₀:", value=3.0)

    # Evaluasi fungsi dan turunannya di (x0, y0)
    f_val = float(f.subs({x: x0, y: y0}))
    fx_val = float(fx.subs({x: x0, y: y0}))
    fy_val = float(fy.subs({x: x0, y: y0}))

    st.write(f"Nilai fungsi di titik (x₀, y₀): {f_val}")
    st.write(f"Gradien di titik (x₀, y₀): (∂f/∂x, ∂f/∂y) = ({fx_val}, {fy_val})")

    st.subheader("📈 Grafik Permukaan & Bidang Singgung")

    # Buat meshgrid untuk permukaan dan bidang singgung
    x_vals = np.linspace(x0 - 2, x0 + 2, 50)
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Permukaan asli
    Z = sp.lambdify((x, y), f, "numpy")(X, Y)

    # Bidang singgung di titik (x0, y0)
    Z_tangent = f_val + fx_val * (X - x0) + fy_val * (Y - y0)

    # Plotting 3D
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.7)
    ax.plot_surface(X, Y, Z_tangent, color="red", alpha=0.5)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Permukaan f(x, y) dan bidang singgung di titik (x₀, y₀)")

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
