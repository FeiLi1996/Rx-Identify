from flask import Flask, render_template, flash,request,redirect, url_for, render_template
import os
import urllib.request
from text_detect import detect_text_from_image
from  search_drug_info import image_identifier
from werkzeug.utils import secure_filename
app = Flask(__name__)




UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def tested():
    return [1,2,3,4]


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
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        test = tested()
        detected_information =detect_text_from_image(filename)
      
        #detected_information ['detected_text']
        drug_data = image_identifier('apo042')
        print('herro',drug_data)
        return render_template(
            'index.html',
            filename=filename,
            test =test,
            drug_data= drug_data ,
            detected_text=detected_information['detected_text'],
            detected_confidence=detected_information ['confidence'] 
         )
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    print('hello')
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/test')
def testing():
    return 'hello'


@app.route('/text_input',methods=['POST'])
def handle_text_input():
    print(request.form['imprint'],'testing input')
    drug_data = image_identifier(request.form['imprint'])
    return render_template('index.html', drug_data= drug_data , submit_text_form = True)


if __name__ =="__main__":
    app.run( debug =True)


