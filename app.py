importmport streamlit as st
from services.blob_services import upload_blob
from services.credit_card_services import extract_credit_card_info

def configure_interface():
  st.title("Upload de arquivo Dio - Desafio 1  -  Fake Docs")
  uploaded_file = st.file.uploader("Escolha um arquivo para upload", type=["pdf", "jpg" , "jpeg", "png"])
  if uploaded_file is not None:
    file.name  = uploaded_file.name
    # Enviar para o Blob Storage
    blob_url = upload_blob(uploaded_file, file.name)
    if blob_url:
      st.write("Arquivo enviado com sucesso!")
      credit_card_info= ""# chamar a função de extração de informações do cartão de crédito
      show_image_and_validation(blob_url, credit_card_info)
    else:
      st.write("Erro ao enviar  ao enviar o arquivo {file.name} para o Azure Blob Storage.")