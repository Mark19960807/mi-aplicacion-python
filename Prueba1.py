from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        title = request.form['title']
        campo1 = request.form['campo1']
        campo2 = request.form['campo2']
        
        # Datos del formulario
        data = {
            "Title": title,
            "Campo1": campo1,
            "Campo2": campo2
        }

        url = "https://tu_sitio.sharepoint.com/_api/web/lists/getbytitle('MiLista')/items"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer tu_token_de_autenticación"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            return "Elemento guardado exitosamente"
        else:
            return f"Error: {response.status_code}"

    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)
