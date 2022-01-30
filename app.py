from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)

"""@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    return jsonify(prediction=predict_result(img))"""

@app.route('/predict')
def parse2():
    import main_prog.py
    
    return "ok"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
