import streamlit as st
import pandas as pd
import base64

# DEFINIR VARIABLES
modalidades = ['CEPREUNI', 'ORDINARIO', 'TRASLADO EXTERNO']
universidades = ['UNI']

# TEMARIO
st.write("---")
st.subheader("1. BUSCA TU TEMARIO")
seleccion_modalidad = st.selectbox("Selecciona la modalidad de admisión", modalidades)

temarios = {
    'CEPREUNI': 'pdfs/tcepreuni.pdf',
    'ORDINARIO': 'pdfs/tordinario.pdf',
    'TRASLADO EXTERNO': 'pdfs/tordinario.pdf'
}

# VISUALIZACION DE TEMARIO O PDF
if seleccion_modalidad in temarios:
    st.write("---")
    st.subheader("1. TEMARIO")
    ruta_pdf = temarios[seleccion_modalidad]
    with open(ruta_pdf, "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    st.markdown(f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000"></embed>', unsafe_allow_html=True)

# RECOMENDADOS
st.write("---")
st.subheader("2. RECOMENDADOS")

canales_recomendados = {
    "canal 1": {"imagen": "icanal1.png", "link": "https://www.youtube.com/@GrupoCienciasSanMarcos"},
    "canal 2": {"imagen": "icanal2.png", "link": "https://www.youtube.com/@bastet1490"},
    "canal 3": {"imagen": "icanal3.png", "link": "https://www.youtube.com/@profesortriquero6538"}
}

col1, col2, col3 = st.columns(3)

with col1:
    # Agregar imagen circular y enlace
    st.markdown(f'<img src="{canales_recomendados["canal 1"]["imagen"]}" class="circle-img">', unsafe_allow_html=True)
    st.markdown(f"[{list(canales_recomendados.keys())[0]}]({list(canales_recomendados.values())[0]['link']})")

with col2:
    st.markdown(f'<img src="{canales_recomendados["canal 2"]["imagen"]}" class="circle-img">', unsafe_allow_html=True)
    st.markdown(f"[{list(canales_recomendados.keys())[1]}]({list(canales_recomendados.values())[1]['link']})")

with col3:
    st.markdown(f'<img src="{canales_recomendados["canal 3"]["imagen"]}" class="circle-img">', unsafe_allow_html=True)
    st.markdown(f"[{list(canales_recomendados.keys())[2]}]({list(canales_recomendados.values())[2]['link']})")

#SECCION DE CARRERAS
st.write("---")
st.subheader("3. CARRERAS")

df = pd.read_excel("data/datos_carreras.xlsx")
carrera_seleccionada = st.selectbox("Selecciona la carrera", df["CARRERA"])

if carrera_seleccionada:
    descripcion = df[df["CARRERA"] == carrera_seleccionada]["DESCRIPCION"].values[0]
    st.subheader("Descripción")
    st.write(descripcion)

    malla_curricular = df[df["CARRERA"] == carrera_seleccionada]["MALLA"].values[0]
    st.subheader("Malla curricular")
    st.code(malla_curricular)

# FORMULARIO DE TUTORÍA
st.write("---")
st.subheader("4. TUTORÍA")

class ComunicateTutor:
    def __init__(self):
        self.nombre = ""
        self.whatsapp = ""
        self.carrera = ""
        self.universidad = ""
        self.mensaje = ""
        self.email = ""
    
    def mostrar_contenido(self):
        self.nombre = st.text_input("Identifícate", placeholder="Escribe tu Nombre completo", max_chars=60)
        self.whatsapp = st.text_input("WhatsApp",  placeholder="Numero de telefono",max_chars=9)
        self.universidad = st.selectbox("Escribe la universidad a postular", universidades)
        self.carrera = st.text_input("¿Carrera?", placeholder="¿Carrera?", max_chars=40)
        self.mensaje = st.text_area("Detalles", placeholder="Ejemplo: Llevo dos ciclos intentando...", max_chars=500)
        self.email = st.text_input("Escribe tu email", max_chars=50)
    
formulario = ComunicateTutor()
formulario.mostrar_contenido()

if st.button("Enviar"):
    st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")
