from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from src.models.audio_processor_ci import process_audio as process
from src.models.text_analyzer import analyze_text
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'txt'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            message = 'No file part in the request.'
            return render_template('index.html', message=message)
        file = request.files['file']
        if file.filename == '':
            message = 'No selected file.'
            return render_template('index.html', message=message)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            if filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                insights = analyze_text(text)
            else:
                text = process_audio(file_path)
                insights = analyze_text(text)
                
                
            return render_template('index.html', insights=insights)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080)
