# Quiz Generator 

Contributors:
Aditya Gajjar (KU2407U392)
Prachi Kakdiya (KU2407U432)
Patel Bina; (KU2407U729)

# Quiz Generation from Paragraph using NLP
The project focuses on generating multiple-choice quiz questions from a paragraph of text using Natural Language Processing (NLP). When a user submits a paragraph, the application first splits it into individual sentences using sentence tokenization. Each sentence is then broken into words, and these words are tagged with their grammatical roles using part-of-speech tagging. From these tagged words, important ones—specifically nouns and verbs—are extracted. One of these is selected as the correct answer, while others serve as distractors to form a four-option MCQ. This approach enables automatic quiz generation without manual effort, making it useful for educational or training applications.

# What is NLP and CV and why we used NLP for our quiz generator
NLP (Natural Language Processing) is a branch of artificial intelligence that deals with understanding and processing human language, while CV (Computer Vision) is another AI field that focuses on interpreting and analyzing visual data like images and videos. In this project, NLP is used because the input is in textual format—specifically, paragraphs of natural language. The goal is to extract meaningful words (like nouns and verbs) from sentences to create quiz questions, which falls squarely under NLP tasks such as tokenization and part-of-speech tagging. Computer Vision is not used here because the input and processing are entirely based on text, not images.

# Django for Frontend and Backend Integration
Django is a Python-based web framework that allows seamless integration of frontend and backend functionalities. In this project, Django handles both the rendering of the HTML form (frontend) and the processing of the text (backend). The home() view loads the input page, and upon form submission, the generate_quiz() view processes the text, runs the NLP logic, and dynamically renders a quiz page with the generated questions. Django’s templating system is used to display questions and options, while its routing and view management simplify the handling of user input and responses, making it an ideal full-stack framework for this kind of application.

# Information about nltk model
NLTK (Natural Language Toolkit) is a popular Python library used for working with human language data. In this project, three key components from NLTK are used: the punkt tokenizer for sentence and word splitting, the averaged_perceptron_tagger for part-of-speech tagging, and the stopwords corpus (optionally) to filter out less meaningful words. These resources are stored in a local nltk_data folder after being downloaded using nltk.download(). The POS tagger uses a pre-trained statistical model that assigns grammatical labels to words, which helps in identifying important keywords for quiz generation. These tools make it easy to process text in a structured and meaningful way.
