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
