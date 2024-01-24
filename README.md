# File Upload to Server

## Description

This project is a Flask application for uploading files to a server in my home. I have this application running on my raspberry pi server at my home running to upload files locally using this app.

## Installation

1. Clone the repository: `git clone https://github.com/shashankbhosagi/uploadfiletoserver`
2. Navigate to the project directory: `cd your-repo`
3. Create and activate a virtual environment: `python3 -m venv venvUpload && source venvUpload/bin/activate`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Set the `FLASK_APP` environment variable: `export FLASK_APP=run.py`
2. Start the Flask development server: `flask run`
3. Open your web browser and visit `http://localhost:5000`

---------------------------OR---------------------------------------------

## Run using Docker

- Build the app in docker using below command and create an image named uploadfile

```bash
sudo docker build -t uploadfile .
```

- Run docker container from the image on port run this command

```bash
sudo docker container run -d -p 5000:5000 uploadfile
```

- To Stop docker container 

```bash
sudo docker container ls
```

```bash
sudo docker container stop <starting_letters_of_container_id>
```