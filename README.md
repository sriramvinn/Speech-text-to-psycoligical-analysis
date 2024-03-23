# Sentiment Analysis Web Application

## Overview

This Flask web application performs sentiment analysis on audio and text. It utilizes OpenAI's API for its core features. Due to the high computational resource requirements of the WhisperX model, I opted not to deploy it in the cloud. Instead, I use Deepgram API for cloud-based audio processing and reserve WhisperX for local development, employing different audio processing modules for each environment.

## Local Setup

### Prerequisites

- Python 3.10 or newer
- An active Deepgram API key
- An active HuggingFace API key
- An active OpenAI API key

### Steps to Run Locally

1. **Clone the Repository**

    ```
    git clone https://github.com/sriramvinn/Alindor_test.git
    ```

2. **Navigate to the Project Directory**

    ```
    cd YOUR_PROJECT_DIRECTORY
    ```

3. **Set Up a Virtual Environment**

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install Dependencies**

    ```
    pip install -r requirements.txt
    pip install git+https://github.com/m-bain/whisperx.git 
    ```

5. **Environment Variables**

    Set your OpenAI API key as an environment variable:

    ```
    export ENVIRONMENT=local
    export OPENAI_API_KEY='YOUR_API_KEY_HERE'
    export DEEPGRAM_API_KEY='YOUR_API_KEY_HERE'
    export HUGGINGFACE_KEY='YOUR_API_KEY_HERE'
    ```

6. **Run the Application**

    ```
    python app.py
    ```

## CI/CD Pipeline with GitHub Actions

The project uses GitHub Actions for Continuous Integration and Continuous Delivery. The workflow is triggered on every push to the main branch.

### Continuous Integration

The CI step includes:

- Linting the code.
- Running unit tests.

### Continuous Delivery

The CD step includes:

- Building the Docker image.
- Pushing the image to Amazon ECR.
- Deploying the image on a self-hosted runner.

### Deployment on AWS

The application is deployed on an AWS EC2 instance using a self-hosted runner for GitHub Actions. The deployment steps pull the latest Docker image from Amazon ECR and run it on the EC2 instance.

## Usage

- Access the web interface via `http://localhost:8080` locally or your EC2 instance's public IP address `http://3.8.208.233:8080`.
- Upload an audio file through the web interface.
- The application will process the audio file, perform sentiment analysis, and display the results.

## Challenges Faced

- **Audio to Text**: For local setups, I use Whisper for transcription and Pyannote for speaker identification. Matching the given text example required careful audio processing.
- **CI/CD Pipeline**: Setting up a CI/CD pipeline with GitHub Actions required careful management of AWS credentials and Docker image handling.
- **Cloud requrements**: Both Whisper and Pyannote can run on CPU or GPU. However, the Whisper model (small.en) and Pyannote individually take about 7 minutes and requires over 3 GB of RAM. Ensuring cost-efficiency for real-time use has been a challenge, which is why it's not deployed in EC2.

## Future Enhancements

- **Speech Emotion Recognition**: Integrating a Speech Emotion Recognition (SER) model could deepen psychological insights by analyzing voice and tone.

