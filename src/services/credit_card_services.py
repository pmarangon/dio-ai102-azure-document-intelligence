from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentAnalysisClient
from azure.ai.documentintelligence import AnalyseDocumentRequest

def analyse_credit_card(card_url):
  try:
    credential= AzureKeyCredential(config.KEY)
   document_client = DocumentIntelligenceClient(config.ENDPOINT, credential)
   card_info = document_client.begin_analyse_document("prebuilt-idcard",AnalyseDocumentRequest(url_source=card_url))
   result = card_info.result()
   for document in result.documents:
     fields = document.fields= document.get('fields', {})
       return{
         "card_name": fields.get('CardholerName',{}).get(content),
         "card_number": fields.get(CardNumber, {}).get(content),
         "expiry_date": filds.get(ExpirationDate,{}).get(content),
         "bank_name": fields.get(IssuingBank,{}).get(content),
       }