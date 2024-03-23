import os

# Determine which environment we're in
environment = os.getenv('ENVIRONMENT', 'local').lower()

# Import the appropriate audio processor module
if environment == 'ci':
    from .audio_processor_ci import process_audio as process
else:
    from .audio_processor_local import process_audio as process