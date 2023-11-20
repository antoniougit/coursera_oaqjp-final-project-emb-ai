import unittest
from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test_joy_emotion(self):
        text = "I am glad this happened."
        result = emotion_detection.emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        text = "I am really mad about this."
        result = emotion_detection.emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        text = "I feel disgusted just hearing about this."
        result = emotion_detection.emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        text = "I am so sad about this."
        result = emotion_detection.emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        text = "I am really afraid that this will happen."
        result = emotion_detection.emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
