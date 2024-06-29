import json
from pymongo import MongoClient

def load_textbook_data():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['chatbot_db']
    
    # Load data from JSON file
    with open('../data/textbook.json', 'r') as file:
        data = json.load(file)
    
    # Insert data into MongoDB
    chapters_collection = db['chapters']
    
    for chapter in data['chapters']:
        chapters_collection.insert_one(chapter)

if __name__ == '__main__':
    load_textbook_data()
