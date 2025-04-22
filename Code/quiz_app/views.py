from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.tokenize import sent_tokenize
import random

# Redirects to generate_quiz if Method is POST
def home(request):
    if request.method == 'POST':
        return generate_quiz(request)
    return render(request, 'quiz_app/input.html')

def generate_quiz(request):
    if request.method == 'POST':
        text = request.POST.get('text_content', '')
        if not text:
            return render(request, 'quiz_app/input.html', {'error': 'Please enter some text'})
            
        try:
            sentences = sent_tokenize(text)
            
            # MCQ
            questions = [] # Empty List
            for sentence in sentences[:10]: 
                words = nltk.word_tokenize(sentence)
                tagged = nltk.pos_tag(words)
                
                # Finds Nouns and Verbs
                important_words = [word for word, tag in tagged if tag.startswith(('NN', 'VB'))]
                
                # Correct MCQ Answer
                if important_words and len(important_words) >= 4: 
                    correct_answer = random.choice(important_words)
                    options = [correct_answer]
                    
                    # Random MCQ 
                    available_words = [w for w in important_words if w != correct_answer]
                    if len(available_words) >= 3:
                        random_options = random.sample(available_words, 3)
                        options.extend(random_options)
                        random.shuffle(options)
                        
                        questions.append({
                            'question': f"What is the important word in this sentence: '{sentence}'?",
                            'options': options,
                            'correct_answer': correct_answer
                        })
            
            # If Question is created render quiz.html
            if questions:
                return render(request, 'quiz_app/quiz.html', {'questions': questions})
            else:
                return render(request, 'quiz_app/input.html', {'error': 'Could not generate questions. Please provide more detailed text.'})
                
        except Exception as e:
            return render(request, 'quiz_app/input.html', {'error': f'An error occurred: {str(e)}'})
    
    return render(request, 'quiz_app/input.html', {'error': 'Invalid request method'})
