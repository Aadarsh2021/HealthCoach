from django.shortcuts import render, redirect
from .models import UserProfile, HealthMetric, HealthGoal
from .forms import UserProfileForm
from ml.model import train_model, predict
from sklearn.model_selection import train_test_split
from .voice import recognize_speech_from_mic

def voice_command(request):
    command = recognize_speech_from_mic()
    return render(request, 'core/voice_command.html', {'command': command})
def predictive_analysis(request):
    data = ...  # Load your health data
    X = data[['feature1', 'feature2']]  # Features
    y = data['target']  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    predictions = predict(model, X_test)
    
    return render(request, 'core/predictive_analysis.html', {'predictions': predictions})

def index(request):
    return render(request, 'core/index.html')

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'core/profile.html', {'form': form})

def dashboard(request):
    metrics = HealthMetric.objects.filter(user=request.user)
    return render(request, 'core/dashboard.html', {'metrics': metrics})
