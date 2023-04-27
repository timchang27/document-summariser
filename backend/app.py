from flask import Flask, request
from flask_cors import CORS
from summarise import Summariser
import os
import yaml

app = Flask(__name__)
CORS(app)

with open ("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

OPENAI_API_KEY = config["OPENAI_API_KEY"]

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    filename = file.filename
    # Save the file to the file path
    upload_dir = os.path.join(os.getcwd(), 'uploads', 'pdfs')
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)

    summariser = Summariser(file_path, OPENAI_API_KEY)
    question = "Give me a summary of this document"
    return {"message": f"File uploaded successfully at {file_path}", "answer": f"{summariser.__str__(question=question)}"}

if __name__ == '__main__':
    app.run()
