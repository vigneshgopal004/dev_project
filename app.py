from flask import Flask, request, send_from_directory, render_template_string
import os

UPLOAD_FOLDER = os.path.expanduser("~/ssc/storage/uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HTML_FORM = '''
<!doctype html>
<title>My Cloud - Upload File</title>
<h2>Upload file to my cloud</h2>
<form method="POST" enctype="multipart/form-data">
 <input type="file" name="file">
 <input type="submit" value="Upload">
</form>

<h2>Available file</h2>
<u1>
 {% for filename in files %}
  <li><a href="/download/{{ filename }}">{{ filename }}</a></li>
 {% else %}
   <li>No files uploaded yet.</li>
 {% endfor %}
</ul>
'''
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files.get('file')
        if f and f.filename:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)
            return f"File uploaded successfully: {f.filename}<br><a href='/'>Back</a>"
    files =os.listdir(app.config['UPLOAD_FOLDER'])    
    return render_template_string(HTML_FORM, files=files)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


