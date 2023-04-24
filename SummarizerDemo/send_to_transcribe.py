import boto3
from time import sleep
import requests
import json

def start_job(job_name, media_uri, media_format, language_code, transcribe_client, vocabulary_name=None):
    """
    Starts a transcription job. This function returns as soon as the job is started.
    To get the current status of the job, call get_transcription_job. The job is
    successfully completed when the job status is 'COMPLETED'.
    
    """
    try:
        job_args = {
            'TranscriptionJobName': job_name,
            'Media': {'MediaFileUri': media_uri},
            'MediaFormat': media_format,
            'LanguageCode': language_code,
            'Settings': {"ShowSpeakerLabels": True, "MaxSpeakerLabels":6}
        }
        response = transcribe_client.start_transcription_job(**job_args)
        job = response['TranscriptionJob']
        print("Started transcription job %s." %job_name)
    except ClientError:
        logger.exception("Couldn't start transcription job %s." %job_name)
        raise
    else:
        return job


def get_transcription(job_name, media_uri, media_format="wav"):
    
    # Start transcribe session
    session = boto3.Session(profile_name='summarizer_testing', region_name='us-west-2')
    client = session.client('transcribe')
    
    # Send Job
    job = start_job(job_name, media_uri, media_format, 'en-US', client)
    status = client.get_transcription_job(TranscriptionJobName=job_name)
    
    # Wait for Job
    while status['TranscriptionJob']['TranscriptionJobStatus'] == 'IN_PROGRESS':
        print('.', end="")
        status = client.get_transcription_job(TranscriptionJobName=job_name)
        sleep(10)
    
    # Return Result
    json_file = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    headers = {'Accept': 'application/json'}
    r = requests.get(json_file, headers=headers)
    return  r.json()



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Process audio files")
    parser.add_argument("--audio_uri", help="URI of the audio file to process")
    parser.add_argument("--job_name", help="Name of the job to be processed, must be unique Transcribe Job name in your console")
    
    args = parser.parse_args()
    
    transcript = get_transcription(args.job_name, args.audio_uri)
    
    with open('./transcription.json', 'w') as fid:
        fid.write(json.dumps(transcript))
    
    