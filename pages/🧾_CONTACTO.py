import streamlit as st
st.write("---")
st.subheader("  CONTACTO ")
col1,col2,col3,col4 =st.columns(4)

# Definir los enlaces a tus redes sociales
enlace_youtube = "https://www.youtube.com/channel/UCee5pfQ3b43EZUYHTm7U8HQ"
enlace_whatsapp = "https://wa.link/fgu2s7"
enlace_github = "https://github.com/josue-org-pe"

# Agregar logotipos con enlaces
logo_youtube = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>'.format(enlace_youtube)
logo_whatsapp = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/whatsapp--v4.png"/></a>'.format(enlace_whatsapp)
logo_github = '<a href="{0}"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>'.format(enlace_github)


col1.markdown(logo_youtube, unsafe_allow_html=True)
col2.markdown(logo_whatsapp, unsafe_allow_html=True)
col3.markdown(logo_github, unsafe_allow_html=True)
image_path ="imagenes\yape.png"
col4.image(image_path,width=100,use_column_width=True)
    
    