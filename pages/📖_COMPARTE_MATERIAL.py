import streamlit as st
import base64

with st.container():
    col1, col2 = st.columns([1, 3])
    col1.subheader("2. COMPARTE TU MATERIAL")
    documento = col2.file_uploader("Sube aquí tu material", type=["pdf"], accept_multiple_files=False)
    
    if documento is not None:
        pdf_bytes = documento.read()  # Leer los bytes del PDF
        with open(documento.name, "wb") as f:
            f.write(pdf_bytes)
        col2.success("Archivo guardado exitosamente")
        st.write("---")
        st.subheader("Vista previa del material:")
        st.write("### " + documento.name)
        st.markdown(f'<a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode("utf-8")}" download="{documento.name}">Descargar archivo</a>', unsafe_allow_html=True)
        st.markdown(f"""
            <iframe src="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode("utf-8")}" width="80%" height="800px">
            </iframe>
        """, unsafe_allow_html=True)
