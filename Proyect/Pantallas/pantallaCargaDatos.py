import flet as ft
import os
import pandas as pd

def carga_form():

    txt_codigo = ft.TextField(label="Código")
    txt_cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER)
    dd_ubicacion = ft.Dropdown(
        label="Ubicación",
        options=[
            ft.dropdown.Option("Producción"),
            ft.dropdown.Option("Mecanizado"),
            ft.dropdown.Option("Calidad"),
        ]
    )
    boton = ft.ElevatedButton(
        content=ft.Text("Guardar Registro", color="white"),
        bgcolor="#1976D2",
        width=300
    )
    txt_descripcion = ft.TextField(
        label="Descripcion",
        read_only = True,
        bgcolor = ft.Colors.GREY_50,
        value = "Esperando Codigo",
    )
    #bar_navegacion= ft.NavigationBar = ft.NavigationBarDestination(
    # destinations=[
    #       ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Carga"),
    #      ft.NavigationBarDestination(icon=ft.Icons.BAR_CHART, label="Gráficos"),
    # ],
    #)

    def buscar_nombre(e):
        txt_descripcion.update()
        if txt_codigo.value:
            nombre = obtener_nombre_por_codigo(txt_codigo.value)
            if nombre:
                txt_descripcion.value = nombre
                txt_descripcion.border_color = ft.Colors.GREEN
            else:
                txt_descripcion.value = "Código no encontrado"
                txt_descripcion.border_color = ft.Colors.RED
        else:
            txt_descripcion.value = "Esperando Codigo"
            txt_descripcion.border_color = None

        txt_descripcion.update()

    txt_codigo.on_change = buscar_nombre


    vista = ft.Column( # lo que veremos ( lo acomoda uno debajo del otro )
        controls=[
            ft.Text("EMPRESA - CARGA", size=20, weight="bold"),
            txt_codigo,
            txt_descripcion,
            txt_cantidad,
            dd_ubicacion,
            boton,

        ],
        spacing=12
    )
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    alignment = ft.MainAxisAlignment.CENTER
    # Devolvemos la vista y los widgets si queremos usarlos fuera
    return vista

def obtener_nombre_por_codigo(codigo):
    # 1. Obtiene la carpeta actual ( /Proyect/Pantallas )
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # 2. SUBE UN NIVEL ( va a /Proyect )
    directorio_padre = os.path.dirname(directorio_actual)

    # 3. Entra en BaseDatos y busca el Maestro
    ruta_excel = os.path.join(directorio_padre, "BaseDatos", "Maestro.xlsx")

    #print(f"Buscando Excel en: {ruta_excel}")
    try:
        # Cargamos con limpieza total de nombres
        df = pd.read_excel(ruta_excel, dtype=str)

        # Buscamos el código
        codigo_buscado = str(codigo).strip()
        fila = df[df["codigo"] == codigo_buscado]

        if not fila.empty:
            # Usamos 'item' que es el nombre en tu Excel
            return fila.iloc[0]["item"]

        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None