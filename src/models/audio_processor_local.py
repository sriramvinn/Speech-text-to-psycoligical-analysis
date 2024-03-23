import whisperx
import os
from src.exception import CustomException

model = None
diarize_model = None

def process_audio(audio):
    try:
        model = get_transcribe_model()
        result = model.transcribe(audio)
        diarize_model = get_diarize_model()
        diarize_segments = diarize_model(audio, max_speakers=2)
        result = whisperx.assign_word_speakers(diarize_segments, result)
        conv = ""
        for segment in result['segments']:
            conv += f"[{segment['speaker']}]:{segment['text']}\n"
        return conv

    except Exception as e:
        raise CustomException(e,sys)

def get_transcribe_model():
    try:
        global model
        if model is None:
            model = whisperx.load_model("base", 'cpu', compute_type= 'int8')
        return model

    except Exception as e:
        raise CustomException(e,sys)

def get_diarize_model():
    try:
        global diarize_model
        if diarize_model is None:
            diarize_model = whisperx.DiarizationPipeline(use_auth_token=os.getenv('HUGGINGFACE_KEY'), device= 'cpu')
        return diarize_model
        
    except Exception as e:
        raise CustomException(e,sys)