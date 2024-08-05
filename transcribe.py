# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
import pip



#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "1b59c8a6d42f449a97c9cd54fc78eecc"

# URL of the file to transcribe
FILE_URL = './D:\Project_Enginnering\gangu_jelly_sudio_dataset.mp3/to/gangu_jelly_sudio_datasetS.mp3'

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
