import os
from src.exception import CustomException
from deepgram import DeepgramClient, PrerecordedOptions

model = None
diarize_model = None

def process_audio(audio):
    try:
        deepgram = DeepgramClient(os.getenv('DEEPGRAM_API_KEY'))

        with open(audio, 'rb') as buffer_data:
            payload = { 'buffer': buffer_data }

            options = PrerecordedOptions(
                smart_format=True, model="nova-2", language="en-GB", diarize = True
            )

            response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
            text = process_response(response)
            return text
    
    except Exception as e:
        raise CustomException(e,sys)

def process_response(response):
    try:
        TAG = 'SPEAKER '
        lines = ""
        words = response["results"]["channels"][0]["alternatives"][0]["words"]
        curr_speaker = 0
        curr_line = ''
        for word_struct in words:
            word_speaker = word_struct["speaker"]
            word = word_struct["punctuated_word"]
            if word_speaker == curr_speaker:
                curr_line += ' ' + word
            else:
                tag = TAG + str(curr_speaker) + ':'
                full_line = tag + curr_line + '\n'
                curr_speaker = word_speaker
                lines += full_line
                curr_line = ' ' + word
        lines += f"{TAG}{str(curr_speaker)}:{curr_line}"
        return lines

    except Exception as e:
        raise CustomException(e,sys)