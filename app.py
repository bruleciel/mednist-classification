# IMPORTS
import os

from flask import Flask, render_template, request, redirect

from inference import get_prediction
from commons import format_class_name

app = Flask(__name__)

# PARTIE PAGE D'ACCUEIL
@app.route('/')
def home():
    return render_template("home.html")

# PARTIE MONO TELECHARGEMENT
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("redirection")
            return redirect(request.url)
        file = request.files.get('file') # Un fichier à la fois
        if not file:
            return
        img_bytes = file.read()
        class_name, class_id = get_prediction(image_bytes=img_bytes)
        return render_template('result.html', class_id=class_id,
                               class_name=class_name)
    return render_template('upload.html')

# PARTIE MULTI TELECHARGEMENT
@app.route('/multi-upload', methods = ['GET', 'POST'])
def upload_files():
    resultats = []
    if request.method == 'POST':
        if 'files' not in request.files:
           print("redirection")
           return redirect(request.url)
        files = request.files.getlist("files") # Plusieurs fichiers à la fois
        if not files:
            return
        for file in files:
            img_bytes = file.read()
            class_name, class_id = get_prediction(image_bytes=img_bytes)
            resultats.append([class_name, class_id])
        print("En dehors de la boucle! ")
        print(resultats)
        return render_template('result_multi.html', resultats=resultats)
    return render_template('upload_multi.html')



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
