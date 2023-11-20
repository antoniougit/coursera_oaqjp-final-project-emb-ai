import requests

def emotion_detector(text_to_analyze):
    try:
        # Check if the input text is empty or None
        if not text_to_analyze:
            # If empty, return a dictionary with None values for all keys
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Define the URL, headers, and input JSON for the Watson NLP Library
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input_json = {"raw_document": {"text": text_to_analyze}}

        # Make a POST request to the Watson NLP Library
        response = requests.post(url, headers=headers, json=input_json)

        # Check the status code of the response
        if response.status_code == 200:
            # If successful, parse the JSON response
            result = response.json()

            # Extract the required set of emotions
            emotions = result.get('document', {}).get('emotion', {})

            # Extract the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Return the result in the specified format
            return {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
            # If status code is 400, return a dictionary with None values for all keys
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            # Otherwise print an error message
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        # If an unexpected error occurs, return an error response
        return {'error': str(e)}
