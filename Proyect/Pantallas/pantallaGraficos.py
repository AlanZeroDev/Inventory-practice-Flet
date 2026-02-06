import flet as ft

import matplotlib.pyplot as plt


def carga_Graficos():

    vista_graficos = ft.Column(
        controls=[
            ft.Text("EMPRESA - GRÁFICOS", size=20, weight="bold"),
            ft.TextField(label="Código a buscar"),
            ft.TextField(label="Descripcion", read_only=True, bgcolor =ft.Colors.GREY_50,value = "Esperando Codigo"),
            ft.TextField(label="Intervalo Fecha"),
        ],
        visible=True,
        spacing=12
    )

    return vista_graficos


#def grafico_pie():
    # Datos
#    etiquetas = ["Producción", "Mecanizado", "Calidad"]
#    valores = [30, 50, 20]

   # Crear gráfico
#    fig, ax = plt.subplots()
#    ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', colors=["#1976D2","#FFC107","#4CAF50"])
#    ax.axis("equal")  # Círculo perfecto

    # Guardar en memoria
#    buf = BytesIO()
#    plt.savefig(buf, format="png")
#    plt.close(fig)
#    buf.seek(0)
#    img_base64 = base64.b64encode(buf.read()).decode()
#    return ft.Image(src=f"data:image/png;base64,{img_base64}")