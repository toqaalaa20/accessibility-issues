from flask import Flask, request, jsonify, render_template
from model import Model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return render_template('index.html', result="No image file provided.")
    
    image_file = request.files['image']
    question = request.form.get('question')
    
    # Assume the image is saved in the same directory for simplicity
    image_path = "uploaded_image.png"
    image_file.save(image_path)

    prompt =f"""<image>\n{question}"""
    
    # Get response from the model
    response = Model().query(image_path, prompt)
    
    return render_template('index.html', result=response)

if __name__ == "__main__":
    app.run(debug=True)
