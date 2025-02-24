
from pymongo import MongoClient

# Connexion à MongoDB
def connect_to_mongo():
    try:
        client = MongoClient('mongodb://127.0.0.1:27017/')
        db = client['diplomas']
        collection = db['extracted_data']
        return collection
    except Exception as e:
        print(f"Erreur de connexion à MongoDB : {e}")
        return None

def store_diploma_in_mongodb(data):
    collection = connect_to_mongo()
    if collection is not None:  
        try:
            collection.insert_one(data)
            return "Données du diplôme enregistrées avec succès dans MongoDB"
        except Exception as e:
            return f"Erreur lors de l'enregistrement des données : {str(e)}"
    else:
        return "Échec de la connexion à MongoDB"



