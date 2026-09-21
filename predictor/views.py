from django.shortcuts import render
from .forms import EmotionForm
from .ml.predictor import predict_emotion
from .models import EmotionAnalysis


def home(request):
    prediction = None
    text = ""

    if request.method == "POST":
        text = request.POST.get("text", "")

        if text.strip():
            prediction = predict_emotion(text)

    return render(
        request,
        "predictor/home.html",
        {
            "emotion": prediction,
            "text": text,
        }
    )
def history(request):
    analyses = EmotionAnalysis.objects.all().order_by("-created_at")

    return render(
        request,
        "predictor/history.html",
        {"analyses": analyses}
    )