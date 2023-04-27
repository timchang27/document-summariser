import yaml
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

class Summariser:
    def __init__(self, pdf_path, openai_api_key):
        self.pdf_path = pdf_path
        self.openai_api_key = openai_api_key

    def summarise(self, question):
        # with open ("config.yaml") as f:
        #     config = yaml.load(f, Loader=yaml.FullLoader)
        OPENAI_API_KEY = self.openai_api_key
        
        reader = PdfReader(self.pdf_path)
        
        raw_text =''
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text

        text_splitter = CharacterTextSplitter(        
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200,
            length_function = len,
        )
        texts = text_splitter.split_text(raw_text)
        # Generate embeddings for the text
        embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)
        # Create vector search using FAISS
        docsearch = FAISS.from_texts(texts, embeddings)
        # Load question answering model
        chain = load_qa_chain(OpenAI(openai_api_key = OPENAI_API_KEY), chain_type="stuff")
        
        # Run question answering model on documents
        docs = docsearch.similarity_search(question)
        ans = chain.run(input_documents=docs, question=question)
        return ans
    
    def __str__(self,question) -> str:
        return f'{self.summarise(question)}'
    
if __name__ == '__main__':
    pdf_path = "CZ4031_Project2_Group17.pdf"
    
    with open ("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    OPENAI_API_KEY = config["OPENAI_API_KEY"]
    
    openai_api_key = OPENAI_API_KEY
    
    s = Summariser(pdf_path, openai_api_key)
    #question = "what are the names of the authors of the article?"
    question = "what is the title of the article?"
    print(s.__str__())