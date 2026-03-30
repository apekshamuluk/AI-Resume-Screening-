# 2] Extract Text from PDF.

import PyPDF2

def extract_text(file_path):
    text = ""
    
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for page in reader.pages:
            try:
                text += page.extract_text()
            except:
                pass
    
    return text
 