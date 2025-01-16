from .BaseController import BaseController
from .ProjectController import ProjectController
from models import ProcessingEnum

import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class ProcessController(BaseController):
    def __init__(self,project_id):
        super().__init__()
        self.project_path = ProjectController().get_project_path(project_id=project_id)
        
    def get_file_extension(self,file_id:str):
        #file_id is the same as file_name ,exemple ran0uvron08k_CVChouaibBouananefr.pdf
        return os.path.splitext(file_id)[-1]
    
    def get_file_loader(self, file_id:str):
        file_ext = self.get_file_extension(file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )
        
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        elif file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None

    def get_fie_content(self, file_id):
        loader = self.get_file_loader(file_id=file_id)
        return loader.load()
    
    def process_file_content(self, file_content: list, file_id: str,
                             overlap_size: int=20, chunk_size: int=100):
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
        )
        
        file_content_texts = [
            rec.page_content
            for rec in file_content
        ] 
        
        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]
        
        chunks = text_splitter.create_documents(
            texts=file_content_texts,
            metadatas=file_content_metadata
        )
        return chunks
        