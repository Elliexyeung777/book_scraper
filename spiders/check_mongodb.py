import pymongo
print(pymongo.__version__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bookscraper"]
collection = db["books"]

# Count documents
print(f"Number of documents: {collection.count_documents({})}")

# Display first 5 documents
print("First 5 documents:")
for doc in collection.find().limit(5):
    print(doc)