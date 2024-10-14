### 1. Funtion:
  - upload PDF file
### 2. Sructure:
```
uploadPDF(Drag and drop)/
│
├── app.py                   # Flask 應用主程式
├── uploads/                 # 用來儲存上傳的檔案
└── templates/
    └── index.html           # 前端 HTML 檔案
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
