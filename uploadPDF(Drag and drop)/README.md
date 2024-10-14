- [Download zipfile](https://github.com/41171119H/SE_weekly_task/blob/main/uploadPDF(Drag%20and%20drop).zip)
### 1. Funtion:
  - upload PDF file
### 2. Sructure:
```
uploadPDF(Drag and drop)/
│
├── venv
├── app.py                   
├── uploads/                
└── templates/
    └── index.html           
```
### 3. Start up:
```
python app.py
```
  - on terminal (powershell) :
    ```
    curl.exe -X POST http://127.0.0.1:5000/api/upload -F "file=@<filename>.pdf"
    ```
    - the terminal will show :
    ```
    {
      "filename": "<filename>.pdf",
      "message": "File uploaded successfully"
    } 
    ```
  - on index.html :  <http://127.0.0.1:5000>
    - If the file uploaded successfully, it would be able to click and view. 
