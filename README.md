# File Insight
File Insight is a web application designed for file analysis. Built on the RESTful architecture, it provides users with essential tools to assess and evaluate files effectively.

## Key Features
- **Magic Number-based Extension Detection**: Enables precise identification of file types, even when filenames or extensions are altered.

- **VirusTotal API File Scanning**: Allows users to scan files for potential threats associated with malicious software using the VirusTotal API.

- **File Comparison using Hashing**: Facilitates quick and reliable file identity verification through hashing functions.

## Screenshots
| Home Page | Magic Numbers |
| -------|--------------|
| <img src="https://github.com/Dawid-Nowotny/restful-file-insight/assets/93731073/2a82dd63-942a-41e9-86cf-c144bb3ea84f" width="600">  | <img src="https://github.com/Dawid-Nowotny/restful-file-insight/assets/93731073/d2963041-50e4-462c-b17c-3efdc921c089" width="600"> |

| File Scan | File Comparison |
| --------------|--------------|
| <img src="https://github.com/Dawid-Nowotny/restful-file-insight/assets/93731073/f3fd1382-5e9e-4166-9283-fb6cff3f6770" width="600">  | <img src="https://github.com/Dawid-Nowotny/restful-file-insight/assets/93731073/586a7436-ead7-4b99-bb0e-4904ec1ca801" width="600"> |

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.8 or later
- Pip
- Node.js + npm: ^14.20.0 || ^16.13.0 || ^18.10.0
- Angular CLI: Angular version 15.2.x
- VirusTotal API Key: A  API key from VirusTotal is required for file scanning functionality

### Installing
Clone the repository:
```bash
git clone https://github.com/Dawid-Nowotny/restful-file-insight.git
```

#### Backend
1. Navigate to the backend folder:
    ```bash
    cd backend
    ```

2. In the file `/backend/src/file/api_key.py`, you will find the variable `VT_API_KEY`. Enter your own VirusTotal API key within the quotation marks, e.g.:
    ```python
    VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"
    ```

3. (Optional) Create a virtual environment (recommended):
    ```bash
    # Windows
    python -m venv venv

    # Linux/macOS
    python3 -m venv venv
    ```

    Activate the virtual environment
    ```bash
    # Windows
    venv\Scripts\activate
    
    # Linux/macOS
    source venv/bin/activate
    ```

4. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
   ```bash
   cd src
   uvicorn main:app
   ```

#### Frontend
1. Navigate to the frontend folder:
    ```bash
    cd frontend
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Run the Angular application:
    ```bash
    ng serve
    ```
