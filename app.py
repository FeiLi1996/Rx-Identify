from flask import Flask, render_template, flash,request,redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename


from text_detect import detect_text_from_image
from  search_drug_info import image_identifier
from config import ApplicationConfig,allowed_file


app = Flask(__name__)

app.config.from_object(ApplicationConfig)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024





@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Image successfully uploaded and displayed below')
        detected_information =detect_text_from_image(filename)
        drug_data = image_identifier(detected_information['detected_text'],'0')

        return render_template(
            'index.html',
            filename=filename,
            drug_data= drug_data ,
            detected_text=detected_information['detected_text'],
            detected_confidence=detected_information ['confidence'] 
         )
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/text_input',methods=['POST'])
def handle_text_input():
    drug_data = image_identifier(request.form['imprint'],request.form['shape'])
    return render_template('index.html', drug_data= drug_data , submit_text_form = True)
if __name__ =="__main__":
    app.run( debug =True)


