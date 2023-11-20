"""
This is a simple Flask application for emotion detection.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Endpoint for emotion detection.

    This function receives a POST request with a JSON payload containing the text to analyze.

    Returns:
        JSON: The result of emotion detection.
    """
    # Get the text to analyze from the request
    text_to_analyze = request.json.get('text')

    # Use the emotion_detector function from the EmotionDetection package
    result = emotion_detection.emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({'message': 'Invalid text! Please try again!'})

    # Return the result in the specified format
    return jsonify(result)

if __name__ == '__main__':
    # Run the application on localhost:5000
    app.run(debug=True)
