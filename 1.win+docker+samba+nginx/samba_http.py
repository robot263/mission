from flask import Flask, request
from smb.SMBConnection import SMBConnection
from io import BytesIO

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    content = file.read()

    conn = SMBConnection('smbuser', 'qaws1234', 'client', '', use_ntlm_v2=True)
    assert conn.connect('127.0.0.1', 445)

    conn.storeFile('smbshare', filename, BytesIO(content))
    conn.close()

    return 'Uploaded to Samba successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

