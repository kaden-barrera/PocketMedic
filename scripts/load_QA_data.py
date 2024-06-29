import json
from pymongo import MongoClient

def load_QA_data():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['chatbot_db']
    
    # Load data from JSON file
    with open('../data/QA.json', 'r') as file:
        data = json.load(file)
    
    # Insert data into MongoDB
    questions_collection = db['questions']
    
    questions_collection.insert_many(data['questions'])

if __name__ == '__main__':
    load_QA_data()
