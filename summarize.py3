import os
import requests
from orq_ai_sdk import OrqAI
from dotenv import load_dotenv

load_dotenv()

# Store the API key as a variable
API_KEY = os.environ.get("ORQ_API_KEY", "")

# Initialize Orq client
client = OrqAI(
    api_key=API_KEY,
    environment="production"
)

# API details
url = "https://my.orq.ai/v2/files"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Specify the folder containing PDF files
folder_path = '/home/peter/projects/un/genai/pdf'
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')][:3]

# Store JSON responses
responses_json = []

for file_name in pdf_files:
    file_path = os.path.join(folder_path, file_name)

    try:
        with open(file_path, 'rb') as file:
            files = {
                'purpose': (None, 'retrieval'),
                'file': (file_name, file)
            }
            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 200:
                responses_json.append(response.json())
                print(f"Successfully uploaded: {file_name}")
            else:
                print(f"Failed to upload: {file_name}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

# Get file ids
file_ids = [response.get('_id') for response in responses_json if response.get('_id')]
print(f"Extracted file IDs: {file_ids}")

for file_id in file_ids:
    try:
        generation = client.deployments.invoke(
            key="peter_pdf",
            context={"environments": []},
            file_ids=[file_id],
            inputs={"words": "500"}
        )
        print(f"Extraction results for {file_id}: {generation.choices[0].message.content}")
    except Exception as e:
        print(f"Error processing {file_id}: {e}")