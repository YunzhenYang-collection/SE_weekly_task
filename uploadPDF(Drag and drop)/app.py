import os
from flask import Flask, request, render_template, jsonify, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf'}

# 檢查檔案類型是否允許
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 儲存檔案
def save_file(file):
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename
    return None

# 首頁：顯示 HTML 表單
@app.route('/')
def index():
    return render_template('index.html')

# API: 上傳檔案處理
@app.route('/api/upload', methods=['POST'])
def upload_file():
    # 檢查是否有文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 檢查是否有文件選擇
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 儲存檔案
    filename = save_file(file)
    if filename:
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# API 回傳以及顯示上傳的檔案:
@app.route('/api/uploads/<filename>', methods=['GET'])
def get_uploaded_file(filename):
    # 確認檔案存在
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    # 確認資料夾已經存在:
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)
