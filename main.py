from flask import Flask, render_template
from google.cloud import storage

app = Flask(__name__)

@app.route('/')
def index():
    # Replace with your Google Cloud Storage bucket and image name
    bucket_name = 'my-app-bucket4'
    image_name = 'myimage.jpg'

    # Construct the image URL
    image_url = f'https://storage.cloud.google.com/{bucket_name}/{image_name}'

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
