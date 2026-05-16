from EmotionDetection import emotion_detector

def test_emotion_detector():

    test_1 = emotion_detector("I am glad this happened")
    assert test_1['dominant_emotion'] == 'joy'

    test_2 = emotion_detector("I am really mad about this")
    assert test_2['dominant_emotion'] == 'anger'

    test_3 = emotion_detector("I feel disgusted just hearing about this")
    assert test_3['dominant_emotion'] == 'disgust'

    test_4 = emotion_detector("I am so sad about this")
    assert test_4['dominant_emotion'] == 'sadness'

    test_5 = emotion_detector("I am really afraid that this will happen")
    assert test_5['dominant_emotion'] == 'fear'

    print("All tests passed!")

test_emotion_detector()
