Features
User Authentication: Secure user registration and login.
ECDSA Digital Signatures: Generates and verifies signatures for patient reports.
PDF Generation: Creates detailed patient reports with QR code signatures.
Signature Verification: Ensures report authenticity with ECDSA.
MySQL Integration: Stores user and report data securely.
Requirements
Python 3.8+
Flask
Flask-MySQLdb
FPDF
pyqrcode
ecdsa
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/repository-name.git
cd repository-name
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up MySQL database:

Create a database named lab.
Execute the necessary SQL commands to create tables for users and reports.
Configure environment variables: Update MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DB in the script.

Run the application:

bash
Copy code
python app.py
Usage
Register or log in as a user.
Create a patient report by providing patient details.
Download the report as a signed PDF with a QR code.
Verify report authenticity using the signature and patient data.
File Structure
app.py: The main application file.
templates/: HTML templates for the user interface.
static/: Static assets like CSS and JS files.
requirements.txt: Python dependencies.
Technologies Used
Flask (Python)
MySQL
ECDSA for Digital Signatures
FPDF for PDF Generation
QR Code Integration
