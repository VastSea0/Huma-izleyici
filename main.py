from flask import Flask, request
import json

app = Flask(__name__)

@app.before_request
def log_request_info():
    # İstek verilerini bir sözlük olarak topla
    request_data = {
        'method': request.method,
        'path': request.path,
        'headers': dict(request.headers),
        'body': request.get_data(as_text=True)
    }
    
    # Gelen veriyi telemetry_data.json dosyasına kaydet
    with open('telemetry_data.json', 'a') as f:
        json.dump(request_data, f)
        f.write('\n')  # Her kaydın yeni bir satırda olması için

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
