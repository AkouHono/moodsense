# 🧠 MoodSense — AI Emotion Detection

MoodSense is an AI-powered web application that detects emotions from natural language text.

The project combines Natural Language Processing (NLP), Deep Learning, and Django to analyze a user's text and classify it into one of six emotions:

- 😊 Joy
- 😢 Sadness
- 😡 Anger
- 😨 Fear
- ❤️ Love
- 😲 Surprise

## 🚀 Project Overview

MoodSense was developed to explore how modern NLP models can understand emotional context in human language.

The project started with a traditional Machine Learning baseline using TF-IDF + Linear SVM and was later improved using a fine-tuned DistilBERT model.

### Model Evolution

| Model | Test Performance |
|---|---:|
| TF-IDF + Linear SVM | 89.85% |
| DistilBERT | 92.65% |

A separate evaluation using 30 manually written natural-language sentences achieved:

**28/30 correct — 93.33% accuracy**

This evaluation was also used for error analysis, particularly for the `surprise` emotion.

## 🤖 Machine Learning

### Baseline Model

The initial model uses:

- TF-IDF Vectorization
- Linear Support Vector Machine (LinearSVC)
- NLTK preprocessing
- Scikit-learn

Pipeline:

Text → Preprocessing → TF-IDF → Linear SVM → Emotion

### Final Model

The final MoodSense model uses:

- DistilBERT
- Hugging Face Transformers
- PyTorch
- Fine-tuning for text classification

Pipeline:

Text → Tokenization → DistilBERT → Classification Head → Emotion

The model was fine-tuned for six emotion classes:

```text
anger
fear
joy
love
sadness
surprise
```

## 📊 Model Performance

The DistilBERT model achieved approximately **92.65% accuracy on the 2,000-sample test set**.

Performance by emotion:

| Emotion | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Anger | 0.92 | 0.93 | 0.92 |
| Fear | 0.90 | 0.92 | 0.91 |
| Joy | 0.95 | 0.94 | 0.94 |
| Love | 0.80 | 0.87 | 0.83 |
| Sadness | 0.96 | 0.97 | 0.96 |
| Surprise | 0.90 | 0.58 | 0.70 |

The results show that the model performs strongly across most classes, while `surprise` remains the most challenging emotion to classify consistently.

## 🖥️ Web Application

The application is built with Django.

Users can:

1. Enter a sentence describing their feelings.
2. Submit the text for analysis.
3. Receive a predicted emotion.
4. View previous emotion analyses through the history interface.

Example:

```text
Input:
"I deeply love my family."

Prediction:
❤️ Love
```

## 🗄️ Database

Django's ORM is used to manage emotion analysis records.

The application can store information such as:

- User/customer input
- Predicted emotion
- Analysis timestamp

The project is designed so that the development database can later be migrated to a production database such as PostgreSQL.

## 🎨 Frontend

The interface was designed to provide a simple and modern user experience.

Technologies include:

- HTML5
- CSS3
- Django Templates
- Responsive design
- CSS animations
- Gradient-based UI
- Emotion-specific visual feedback

## 🛠️ Technology Stack

### Backend
- Python
- Django
- Django ORM

### Machine Learning / NLP
- PyTorch
- Hugging Face Transformers
- DistilBERT
- Scikit-learn
- NLTK
- NumPy

### Frontend
- HTML5
- CSS3
- Django Templates

### Database
- SQLite for development
- PostgreSQL planned for production

### Development Tools
- Git
- GitHub
- VS Code
- Python Virtual Environment

## 📁 Project Structure

```text
moodsense/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── moodsense/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── predictor/
│   ├── migrations/
│   ├── templates/
│   │   └── predictor/
│   │       ├── home.html
│   │       └── history.html
│   │
│   ├── ml/
│   │   ├── predictor.py
│   │   └── distilbert/
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
└── ...
```

> Note: The trained DistilBERT model weights are kept private and are not included in this public repository.

## 🔐 Model Security

The trained model is intentionally excluded from the public GitHub repository.

The repository contains the application architecture and inference code, while the trained model weights remain in private storage.

This prevents unauthorized access or reuse of the trained model.

## 🔮 Future Improvements

- [ ] Production deployment
- [ ] PostgreSQL integration
- [ ] Secure private model hosting
- [ ] Confidence scores
- [ ] Improved surprise-emotion classification
- [ ] User authentication
- [ ] Emotion analytics dashboard
- [ ] Multilingual emotion detection
- [ ] API endpoint for external applications
- [ ] Mobile application integration

## 🎯 Project Goals

MoodSense is both a practical AI application and a learning project focused on:

- Natural Language Processing
- Transformer-based models
- Model evaluation
- Error analysis
- Machine Learning deployment
- Django development
- AI application architecture

## 👩🏾‍💻 Author

**Yémima Honorine**

MSc Computer Science | AI & Machine Learning

Interested in Machine Learning Engineering, NLP, Data Science and AI-powered applications.

email: autoflowc@gmail.com

## 🏷️ GitHub Topics

python, django, machine-learning, deep-learning, nlp, distilbert, transformers, pytorch, scikit-learn, emotion-detection, natural-language-processing, artificial-intelligence
