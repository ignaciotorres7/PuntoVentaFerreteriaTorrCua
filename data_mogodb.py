from pymongo import MongoClient


def get_connection_Database():
    """
    Establishes a connection to the MongoDB database and returns the database object.
    """
    try:
        # Connect to the MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        # Access the 'mydatabase' database
        db = client['FerreteriaTorr_Cua']
        return db
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None
    
def get_collection(db, collection_name):
    """
    Retrieves a collection from the specified database.
    
    :param db: The database object.
    :param collection_name: The name of the collection to retrieve.
    :return: The collection object or None if the collection does not exist.
    """
    try:
        collection = db[collection_name]
        return collection
    except Exception as e:
        print(f"An error occurred while accessing the collection '{collection_name}': {e}")
        return None
    
def insert_document(collection, document):
    """
    Inserts a document into the specified collection.
    
    :param collection: The collection object.
    :param document: The document to insert.
    :return: The result of the insertion operation.
    """
    try:
        result = collection.insert_one(document)
        return result
    except Exception as e:
        print(f"An error occurred while inserting the document: {e}")
        return None
    
def find_documents(collection, query=None):
    """
    Finds documents in the specified collection based on the query.
    
    :param collection: The collection object.
    :param query: The query to filter documents (default is None, which retrieves all documents).
    :return: A list of documents matching the query.
    """
    try:
        if query is None:
            query = {}
        documents = list(collection.find(query))
        return documents
    except Exception as e:
        print(f"An error occurred while finding documents: {e}")
        return None
    
def update_document(collection, query, update):
    """
    Updates documents in the specified collection based on the query.
    
    :param collection: The collection object.
    :param query: The query to filter documents to update.
    :param update: The update operation to apply.
    :return: The result of the update operation.
    """
    try:
        result = collection.update_many(query, update)
        return result
    except Exception as e:
        print(f"An error occurred while updating documents: {e}")
        return None
    
def delete_document(collection, query):
    """
    Deletes documents from the specified collection based on the query.
    
    :param collection: The collection object.
    :param query: The query to filter documents to delete.
    :return: The result of the deletion operation.
    """
    try:
        result = collection.delete_many(query)
        return result
    except Exception as e:
        print(f"An error occurred while deleting documents: {e}")
        return None
    
def insert_multiple_documents(collection, documents):
    """
    Inserts multiple documents into the specified collection.
    
    :param collection: The collection object.
    :param documents: A list of documents to insert.
    :return: The result of the insertion operation.
    """
    try:
        result = collection.insert_many(documents)
        return result
    except Exception as e:
        print(f"An error occurred while inserting multiple documents: {e}")
        return None
    
def logical_delete_document(collection, query):
    """
    Performs a logical delete by updating a 'activo' field in the specified collection.
    
    :param collection: The collection object.
    :param query: The query to filter documents to logically delete.
    :return: The result of the logical delete operation.
    """
    try:
        update = {"$set": {"activo": False}}
        result = collection.update_many(query, update)
        return result
    except Exception as e:
        print(f"An error occurred while performing a logical delete: {e}")
        return None
    
def close_connection(client):
    """
    Closes the connection to the MongoDB server.
    
    :param client: The MongoClient object.
    """
    try:
        client.close()
    except Exception as e:
        print(f"An error occurred while closing the connection: {e}")   
