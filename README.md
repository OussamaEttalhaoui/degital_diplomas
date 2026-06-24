#  Digitalization of Academic Diplomas using NLP & Blockchain

##  Overview
This project automates and secures academic diploma management by combining **Natural Language Processing (NLP)** and **blockchain technology**.  
Diploma information is automatically extracted from images or PDF files and securely registered on the blockchain to ensure **authenticity, integrity, and traceability**.

---

##  Technologies
- **Ethereum (Ganache, Truffle)** – Smart contracts  
- **Web3.py** – Blockchain interaction  
- **Streamlit** – User interface  
- **MongoDB** – Data validation  
- **BERT (NLP) + OCR (Tesseract)** – Information extraction  
- **PDFPlumber & ReportLab** – PDF processing and generation  

---

##  Key Features
- Extract diploma data from images and PDFs  
- NLP-based information extraction using BERT  
- Secure diploma storage on the blockchain  
- User validation before blockchain registration  
- Generation of a verified PDF with blockchain transaction ID  

---

##  Workflow
1. Upload diploma (image or PDF)  
2. OCR + NLP data extraction  
3. Data validation (MongoDB)  
4. User review & correction  
5. Blockchain registration  
6. Verified PDF generation  

---

##  Installation & Setup

### Prerequisites
- Python 3.x  
- Node.js & npm  
- Ganache (local blockchain)  
- Truffle  
- MongoDB (local)

---

### Install Dependencies and Run the Project
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Blockchain tools
npm install -g truffle

# Deploy Smart Contracts
cd blockchain
npm install
truffle compile
truffle migrate

# Copy the deployed contract address and add it to the .env file

# Launch the Streamlit App
cd ../frontend
streamlit run streamlit_app.py

## 🛠️ Realization

After launching the project, the main interface allows users to upload a diploma file (PDF or image) for digital processing.
---

### 📌 Main Interface
The user can upload a diploma to start the extraction and digitization process.

<img width="456" height="218" alt="image" src="https://github.com/user-attachments/assets/f073b49b-1364-4e96-b836-1d0f00aba45e" />

---

### 📄 Information Extraction
After upload, all diploma data is automatically extracted using OCR and NLP, then structured into a readable table.

<img width="456" height="260" alt="image" src="https://github.com/user-attachments/assets/7ffd00ff-bfa7-49c8-adbd-f21929d1c28e" />

---

### ✏️ Data Review & Correction
Users can review and correct extracted information to ensure accuracy before validation.

<img width="456" height="258" alt="image" src="https://github.com/user-attachments/assets/da27fb1d-6110-4a26-9aee-df5f06c5dc30" />

---

### ⛓️ Blockchain Registration
Once validated, the data is stored on the blockchain and also saved in MongoDB for centralized access.

A button allows the user to register the data on the blockchain.

<img width="456" height="246" alt="image" src="https://github.com/user-attachments/assets/67a24c75-923c-4a3a-9be6-bd671924394f" />

---

### 📄 Verified PDF Generation
After successful registration, a downloadable PDF is generated containing:
- Extracted diploma information  
- Blockchain transaction ID  

<img width="456" height="269" alt="image" src="https://github.com/user-attachments/assets/85bb0290-84f6-4935-8265-d0a3e8e9c466" />

---

### 🔍 Ganache Transaction Verification
Transactions can be verified using Ganache, showing all blockchain records.

<img width="454" height="242" alt="image" src="https://github.com/user-attachments/assets/d9e1a6f3-7937-4aac-84c8-1d0c5eaf5c6a" />

---

### 🗄️ MongoDB Storage
All validated diploma data is stored in MongoDB in a structured format for future use and retrieval.

<img width="454" height="215" alt="image" src="https://github.com/user-attachments/assets/6b73aac2-9a4e-493f-bf3a-09ff4b593c08" />
