import streamlit as st

# Definir las universidades disponibles
universidades = ['UNI', 'Otra Universidad', 'Otra Universidad 2']

class ComunicateTutor:
    def __init__(self) -> None:
        self.nombre = ""
        self.whatsapp = ""
        self.universidad = ""
        self.mensaje = ""
        self.email = ""
    
    def mostrar_contenido(self):
        self.nombre = st.text_input("Identifícate", placeholder="Escribe tu Nombre completo", max_chars=60)
        self.whatsapp = st.text_input("WhatsApp",  placeholder="Número de teléfono", max_chars=9)
        self.universidad = st.selectbox("Escribe la universidad a postular", universidades)
        self.carrera = st.text_input("¿Carrera?", placeholder="¿Carrera?", max_chars=40)
        self.mensaje = st.text_input("Detalles", placeholder="Ejemplo: Llevo dos ciclos intentando...", max_chars=500)
        self.email = st.text_input("Escribe tu email", max_chars=50)

st.subheader("3. TUTORIA")
formulario = ComunicateTutor()
formulario.mostrar_contenido()
    
if st.button("Enviar"):
    st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")
