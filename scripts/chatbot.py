from pymongo import MongoClient
from functools import lru_cache

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']

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
