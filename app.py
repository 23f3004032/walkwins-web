from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'kingsman-space-services-2025'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year cache for static files

@app.route('/')
def index():
    """Main landing page route"""
    return render_template('index.html')

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)