# Gesture Recognition Web Application

This project is a web application built using Python Flask that allows users to upload an image or a video for gesture recognition. The uploaded media is processed through a pre-trained machine learning model, which classifies the gesture and returns the result. The web application is designed to be interactive and user-friendly, with a clean and modern interface.

## Features

- **Image Upload**: Users can upload an image, which is then processed to identify the gesture.
- **Video Upload**: Users can upload a video, which is analyzed frame by frame to detect gestures.
- **Real-time Feedback**: The application provides immediate feedback on the detected gestures.
- **Responsive Design**: The web app is fully responsive, ensuring a seamless experience across devices.
- **Interactive UI**: The UI is designed with interactivity in mind, using images from Unsplash and dynamic effects.

## Project Structure

The project is structured as follows:

    gesture_recognition/
    │
    ├── app/
    │ ├── init.py 
    │ ├── routes.py
    │ ├── static/ 
    │ │ ├── css/
    │ │ │ └── style.css 
    │ │ ├── js/
    │ │ │ └── scripts.js 
    │ │ └── images/ 
    │ └── templates/ 
    │ ├── layout.html 
    │ ├── index.html 
    │ ├── image_analysis.html 
    │ ├── video_analysis.html 
    │
    ├── helpers/
    │ ├── init.py 
    │ ├── image_analysis.py 
    │ └── video_analysis.py 
    │
    ├── uploads/
    │ ├── images/ 
    │ └── videos/ 
    │
    ├── run.py 
    └── requirements.txt 


## Installation

### Prerequisites

- Python 3.7+
- Virtual Environment (recommended)
- Flask

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/gesture-recognition-webapp.git
   cd gesture-recognition-webapp
   ```
2. **Create a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. **Install the dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the Flask app**:
    
    Ensure the Flask app is correctly set up by configuring environment variables if necessary.
    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    ```
5. **Run the application**:
    ```bash
    flask run
    ```
6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
### Uploading an Image
1. Navigate to the homepage.
2. Click on the "Upload Image" button.
3. Select an image file and click "Submit".
4. The image will be processed, and the gesture will be displayed on the image analysis page.

### Uploading a Video

1. Navigate to the homepage.
2. Click on the "Upload Video" button.
3. Select a video file and click "Submit".
4. The video will be analyzed, and the results will be displayed on the video analysis page.

## Customization
### Adding Your Model

- The helpers/image_analysis.py and helpers/video_analysis.py files are designed to integrate your gesture recognition model. Add your model loading and prediction code in these files.

### Static Files

- You can customize the look and feel of the web app by editing the CSS and JS files located in the app/static/ directory.

### Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

### Acknowledgements

- Unsplash for the royalty-free images used in the application.
- Flask community for their continuous support and documentation.


### Key Points in the README:

- **Overview**: Brief description of the project and its purpose.
- **Features**: Highlights the main functionalities of the web application.
- **Project Structure**: Explains the organization of the project files and directories.
- **Installation**: Step-by-step instructions for setting up the project locally.
- **Usage**: Instructions on how to use the web application to upload images and videos.
- **Customization**: Guidance on how to add your machine learning model and customize the static files.
- **Contributing**: Information on how to contribute to the project.
- **License**: Licensing information.
- **Acknowledgements**: Credits to Unsplash for images and the Flask community.
