from predictor.ml.predictor import predict_emotion



test_sentences = [
    # JOY
    ("I am incredibly happy about my graduation!", "joy"),
    ("Today has been the best day of my life.", "joy"),
    ("I received wonderful news and I cannot stop smiling.", "joy"),
    ("I feel so excited and happy about my new opportunity.", "joy"),
    ("Celebrating with my family made me incredibly happy.", "joy"),

    # SADNESS
    ("I miss my family and feel very lonely.", "sadness"),
    ("I cried when I heard the terrible news.", "sadness"),
    ("I feel completely heartbroken after losing my friend.", "sadness"),
    ("Everything feels empty and I cannot stop feeling sad.", "sadness"),
    ("I am devastated by what happened yesterday.", "sadness"),

    # ANGER
    ("I am furious about what they did to me.", "anger"),
    ("This unfair treatment makes me extremely angry.", "anger"),
    ("I cannot believe they treated me so disrespectfully.", "anger"),
    ("I am extremely frustrated with this situation.", "anger"),
    ("Their behavior made me absolutely furious.", "anger"),

    # FEAR
    ("I am terrified that something bad will happen.", "fear"),
    ("I am scared to walk home alone at night.", "fear"),
    ("The thought of failing the exam makes me very afraid.", "fear"),
    ("I was frightened when I heard a strange noise outside.", "fear"),
    ("I feel anxious and afraid about what might happen.", "fear"),

    # LOVE
    ("I deeply love my family and cherish every moment with them.", "love"),
    ("She makes me feel loved, safe, and appreciated.", "love"),
    ("I have so much affection for my best friend.", "love"),
    ("He means everything to me and I love him deeply.", "love"),
    ("I feel a deep connection and love for my family.", "love"),

    # SURPRISE
    ("I couldn't believe it when they gave me the award!", "surprise"),
    ("I was completely shocked by the unexpected news.", "surprise"),
    ("I never expected to receive such an amazing gift.", "surprise"),
    ("I was stunned when I saw what happened.", "surprise"),
    ("The unexpected announcement left me completely amazed.", "surprise"),
]

print("\nMoodSense Evaluation\n")

correct = 0

for text, expected in test_sentences:
    predicted = predict_emotion(text)

    result = "✓" if predicted == expected else "✗"

    if predicted == expected:
        correct += 1

    print(f"{result} Expected: {expected:8} | Predicted: {predicted:8} | {text}")

accuracy = correct / len(test_sentences) * 100

print("\n--------------------------------")
print(f"Correct: {correct}/{len(test_sentences)}")
print(f"Accuracy: {accuracy:.2f}%")