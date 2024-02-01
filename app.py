from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect(url_for('index'))
    
# Route to handle text submissions
@app.route('/upload_text', methods=['POST'])
def upload_text():
    text = request.form['text']

    if text:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'text_submission.txt')
        with open(filename, 'w') as file:
            file.write(text)
        return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
