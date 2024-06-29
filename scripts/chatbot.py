from pymongo import MongoClient
from functools import lru_cache
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def normalize_text(text):
    return text.lower().strip()

def preprocess_text(text):
    words = word_tokenize(text)
    words = [ps.stem(w) for w in words if w.isalnum() and w not in stop_words]
    return ' '.join(words)

# Functions for QA data
@lru_cache(maxsize=32)
def get_question_by_id(question_id):
    questions_collection = db['questions']
    result = questions_collection.find_one({"id": question_id})
    if result:
        return result
    else:
        return "Question not found."

@lru_cache(maxsize=32)
def get_answer(question_id):
    question = get_question_by_id(question_id)
    if question != "Question not found.":
        return question['answer']
    else:
        return "Question not found."

@lru_cache(maxsize=32)
def get_all_questions():
    questions_collection = db['questions']
    results = questions_collection.find()
    return list(results)

# Functions for textbook data
@lru_cache(maxsize=32)
def get_chapter(chapter_number):
    chapters_collection = db['chapters']
    result = chapters_collection.find_one({"chapter_number": chapter_number})
    if result:
        return result
    else:
        return "Chapter not found."

@lru_cache(maxsize=32)
def get_objectives(chapter_number):
    chapter = get_chapter(chapter_number)
    if chapter != "Chapter not found.":
        return chapter['objectives']
    else:
        return "Chapter not found."

@lru_cache(maxsize=32)
def get_content_by_objective(chapter_number, objective):
    chapter = get_chapter(chapter_number)
    if chapter != "Chapter not found.":
        for content in chapter['content']:
            if content['objective'] == objective:
                return content['data']
        return "Objective not found."
    else:
        return "Chapter not found."

@lru_cache(maxsize=32)
def get_miscellaneous_data(chapter_number):
    chapter = get_chapter(chapter_number)
    if chapter != "Chapter not found.":
        return chapter['miscellaneous']
    else:
        return "Chapter not found."

# Example usage
if __name__ == '__main__':
    # QA example
    question_id = 1
    question = get_question_by_id(question_id)
    print(f"Question: {question}")

    answer = get_answer(question_id)
    print(f"Answer: {answer}")

    all_questions = get_all_questions()
    for q in all_questions:
        print(f"Question ID: {q['id']}, Question: {q['question']}, Answer: {q['answer']}")

    # Textbook example
    chapter_number = 1
    chapter = get_chapter(chapter_number)
    print(f"Chapter: {chapter}")
    
    objectives = get_objectives(chapter_number)
    print(f"Objectives: {objectives}")

    objective = "Understand the basic concepts of geography"
    content = get_content_by_objective(chapter_number, objective)
    print(f"Content for objective '{objective}': {content}")

    miscellaneous = get_miscellaneous_data(chapter_number)
    print(f"Miscellaneous Data: {miscellaneous}")
