import streamlit as st
import base64

st.set_page_config(page_title="PrePlaneta🪐", page_icon="👽", layout="wide")

# VARIABLES
universidades = ['UNI', 'UNMSM', 'UNAP']

# SECCION SOBRE NOSOTROS
with st.container():
    st.title("¡Hola causa 👽!")
    st.title("Te brindamos lo que necesitas para tu próxima admisión...")
    st.write("---")
    st.subheader("1. NOSOTROS")
    st.text("""
    Bienvenidos a Preplaneta, tu recurso esencial para preparar los exámenes de admisión universitaria. Aquí encontrarás
    información detallada sobre exámenes, temarios, orientación sobre carreras y una biblioteca.
    Únete a nuestra comunidad y prepárate para conseguir esa vacante.
    """)
    st.write("---")

#FUNCION DE FORMULARIO
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

# Sección "COMPARTE TU MATERIAL"

with st.container():
    col1, col2 = st.columns([1, 3])
    col1.subheader("2. COMPARTE TU MATERIAL")
    documento = col2.file_uploader("Sube aquí tu material", type=["pdf"], accept_multiple_files=False)
    
    if documento is not None:
        pdf_bytes = documento.read()  
        with open(documento.name, "wb") as f:
            f.write(pdf_bytes)
        col2.success("Archivo guardado exitosamente")
        st.write("---")
        st.subheader("Vista previa del material:")
        st.write("### " + documento.name)
        st.download_button(label="Descargar archivo", data=documento, file_name=documento.name)
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
        st.markdown(f"""
            <iframe src="data:application/pdf;base64,{pdf_base64}" width="80%" height="800px">
            </iframe>
        """, unsafe_allow_html=True)

#SECION TUTORIA
st.subheader("3. TUTORIA")
formulario = ComunicateTutor()
formulario.mostrar_contenido()
    
if st.button("Enviar"):
    st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")

# REDES
st.write("---")
st.subheader("CONTACTO")
col1, col2, col3, col4 = st.columns(4)

enlace_youtube = "https://www.youtube.com/channel/UCee5pfQ3b43EZUYHTm7U8HQ"
enlace_whatsapp = "https://wa.link/fgu2s7"
enlace_github = "https://github.com/josue-org-pe"

logo_youtube = f'<a href="{enlace_youtube}"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>'
logo_whatsapp = f'<a href="{enlace_whatsapp}"><img src="https://img.icons8.com/color/48/000000/whatsapp--v4.png"/></a>'
logo_github = f'<a href="{enlace_github}"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>'

col1.markdown(logo_youtube, unsafe_allow_html=True)
col2.markdown(logo_whatsapp, unsafe_allow_html=True)
col3.markdown(logo_github, unsafe_allow_html=True)

image_path = "imagenes/yape.png"
col4.image(image_path, width=100, use_column_width=True)
