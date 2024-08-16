import os
from flask import render_template, request, redirect, url_for, current_app, send_from_directory
from werkzeug.utils import secure_filename
from helpers import analyze_image, analyze_video

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload-image', methods=['POST'])
    def upload_image():
        if 'image' not in request.files:
            return redirect(url_for('index'))

        file = request.files['image']
        if file.filename == '':
            return redirect(url_for('index'))

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER_IMAGES'], filename)
            file.save(filepath)

            # Here, you would call the image analysis function
            result = analyze_image(filepath)
            # result = "gesture_name_placeholder"  # Placeholder

            return render_template('image_analysis.html', image_url=url_for('uploaded_file', filename=filename), result=result)

    @app.route('/upload-video', methods=['POST'])
    def upload_video():
        if 'video' not in request.files:
            return redirect(url_for('index'))

        file = request.files['video']
        if file.filename == '':
            return redirect(url_for('index'))

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER_VIDEOS'], filename)
            file.save(filepath)

            # Here, you would call the video analysis function
            # result = video_analysis_function(filepath)
            result = "gesture_name_placeholder"  # Placeholder

            return render_template('video_analysis.html', video_url=url_for('uploaded_file', filename=filename), result=result)

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            return send_from_directory(current_app.config['UPLOAD_FOLDER_IMAGES'], filename)
        if filename.endswith(('.mp4', '.avi')):
            return send_from_directory(current_app.config['UPLOAD_FOLDER_VIDEOS'], filename)
