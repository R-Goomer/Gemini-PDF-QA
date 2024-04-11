import streamlit as st
from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores.faiss import FAISS

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.chains.question_answering import load_qa_chain

from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


##os.environ['GOOGLE_API_KEY'] = 'AIzaSyBSNGdkNP53deukuMGdh66J-YrYJ4C6J5Q'

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


def get_pdf_text(pdf_file):
  text = ""
  pdf_reader = PdfReader(pdf_file)
  for page in pdf_reader.pages:
    text += page.extract_text()
  return text

def get_text_chunks(text):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000)
  chunks = text_splitter.split_text(text)
  return chunks

def get_vector_store(text_chunks):
  embeddings = GoogleGenerativeAIEmbeddings(model = 'models/embedding-001')
  vector_store = FAISS.from_texts(text_chunks,embedding = embeddings)
  vector_store.save_local("fiass_index.pkl")
  return vector_store

def get_conversational_chain():
  prompt_template = """
  Answer the question as detailed as possible from the provided context, make sure to provide all the details.

  Context: \n {context}?\n
  Question: \n {question}\n

  Answer:
  """

  model = ChatGoogleGenerativeAI(model = "gemini-pro", temperature = 0.3)

  prompt = PromptTemplate(template = prompt_template, input_variables=["context","question"])

  chain = load_qa_chain(model, chain_type = "stuff", prompt = prompt)

  return chain

def user_input(user_question):
  embeddings = GoogleGenerativeAIEmbeddings(model = 'models/embedding-001')

  new_db = FAISS.load_local("fiass_index.pkl", embeddings,  allow_dangerous_deserialization=True)
  docs = new_db.similarity_search(user_question)

  chain = get_conversational_chain()

  response = chain(
      {"input_documents": docs, "question": user_question}, return_only_outputs = True
  )

  print(response)

  st.write("Reply: ", response["output_text"])

def main():
  st.set_page_config("chat with multiple PDF")
  st.header("chat with multiple PDF with Gemini")

  user_question = st.text_input("Ask a Question from the PDF files")

  if user_question:
    user_input(user_question)

  with st.sidebar:
    st.title("Menu:")
    pdf_files = st.file_uploader("Upload you PDF and click on Submit", accept_multiple_files=True)
    if st.button("Submit and Process") and pdf_files:
      with st.spinner("Processing..."):
        raw_text = ""
        for pdf_file in pdf_files:
            raw_text += get_pdf_text(pdf_file)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks)
        st.success("Done")

if __name__ == "__main__":
  main()

