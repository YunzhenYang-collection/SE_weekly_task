import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads' # 文件上傳後的存取資料夾為 "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf'} # 允許上船的格式為 pdf

# 檢查上傳的檔案類型是否正確
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 處理文件上傳到指定資料夾: 
def save_file(file):
    if file and allowed_file(file.filename):  # 檢查file 是否存在
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # 指定資料夾: UPLOAD_FOLDER = 'uploads'
        return filename # 成功
    return None

# the route of Flask:
@app.route('/')
def index():
    return render_template('index.html', message=None)

# 選擇文件上傳處理:
@app.route('/upload', methods=['POST'])
def upload_file():
    # 檢查是否選擇文件
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    # 檢查文件名稱是否為空
    if file.filename == '':
        return 'No selected file'
    
    filename = save_file(file) # 保存文件

    # 顯示檔案上傳成功與否的提示訊息
    if filename:
        return render_template('index.html', message="File uploaded successfully!", filename=filename)
    else:
        return 'File type not allowed.'

# 顯示上傳的文件
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)
