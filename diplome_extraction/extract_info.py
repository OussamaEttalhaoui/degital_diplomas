#extract_info.py
import pytesseract
from PIL import Image
from transformers import pipeline



import pdfplumber


def extract_information_from_image(image_path):
    # Charger le modèle BERT pour le question answering
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    nlp = pipeline("question-answering", model=model_name)

    # Charger l'image et extraire le texte avec Tesseract
    img = Image.open(image_path)
    context = pytesseract.image_to_string(img, lang='eng+ara')
    
    print("Texte extrait de l'image :")
    print(context)  # Vérifier le texte brut extrait

    # Questions à poser avec des formulations plus adaptées
    questions = {
        "Nom de l'étudiant": "Quel est le nom de l'étudiant auquel le diplôme est attester ?",
        "Prénom de l'étudiant": "Quel est le prénom de l'étudiant auquel le diplôme est attester ?",
        "CNE de l'étudiant": "Quel est le CNE de l'étudiant ?",
        "CIN de l'étudiant": "Quel est le numéro de la carte d'identité nationale (CIN) de l'étudiant ?",
        "Diplôme obtenu": "Quel diplôme a été obtenu ?",
        "Spécialisation du diplôme": "Quelle est la spécialisation (filière) du diplôme ?",
        # "Université d'obtention": "Dans quelle université le diplôme est-il obtenu ?",
        "Université d'obtention": "Dans quelle université ?",
        "Année d'obtention": "Quelle est l'année d'obtention du diplôme ?",
        "Mention du diplôme": "Quelle est la mention du diplôme ?"
    }

    # Collecter les réponses
    answers = {}
    for key, question in questions.items():
        result = nlp(question=question, context=context)
        answers[key] = result['answer'] if result['answer'] else "Inconnu"  # Ajouter une vérification pour éviter les réponses vides

    # Recherche de la mention (si le modèle ne la trouve pas, faire une détection par contexte ou texte brut)
    if "Mention du diplôme" not in answers or not answers["Mention du diplôme"]:
        # Tenter une extraction manuelle de la mention dans le texte
        mention_keywords = ["Passable", "Bien", "Très bien", "Excellent"]
        for keyword in mention_keywords:
            if keyword.lower() in context.lower():
                answers["Mention du diplôme"] = keyword
                break
        else:
            answers["Mention du diplôme"] = "Inconnue"  # Valeur par défaut si pas de mention trouvée
    
    return answers


def extract_information_from_pdf(pdf_path):
    # Charger le modèle BERT pour le question answering
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    nlp = pipeline("question-answering", model=model_name)

    # Ouvrir le PDF et extraire le texte
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    print("Texte extrait du PDF :")
    print(text)  # Vérifier le texte brut extrait

    # Questions à poser avec des formulations plus adaptées
    questions = {
        "Nom de l'étudiant": "Quel est le nom de l'étudiant auquel le diplôme est attester ?",
        "Prénom de l'étudiant": "Quel est le prénom de l'étudiant auquel le diplôme est attester ?",
        "CNE de l'étudiant": "Quel est le CNE de l'étudiant ?",
        "CIN de l'étudiant": "Quel est le numéro de la carte d'identité nationale (CIN) de l'étudiant ?",
        "Diplôme obtenu": "Quel diplôme a été obtenu ?",
        "Spécialisation du diplôme": "Quelle est la spécialisation (filière) du diplôme ?",
        "Université d'obtention": "Dans quelle université ?",
        "Année d'obtention": "Quelle est l'année d'obtention du diplôme ?",
        "Mention du diplôme": "Quelle est la mention du diplôme ?"
    }

    # Collecter les réponses
    answers = {}
    for key, question in questions.items():
        result = nlp(question=question, context=text)
        answers[key] = result['answer'] if result['answer'] else "Inconnu"  # Ajouter une vérification pour éviter les réponses vides

    # Recherche de la mention (si le modèle ne la trouve pas, faire une détection par contexte ou texte brut)
    if "Mention du diplôme" not in answers or not answers["Mention du diplôme"]:
        mention_keywords = ["Passable", "Bien", "Très bien", "Excellent"]
        for keyword in mention_keywords:
            if keyword.lower() in text.lower():
                answers["Mention du diplôme"] = keyword
                break
        else:
            answers["Mention du diplôme"] = "Inconnue"  # Valeur par défaut si pas de mention trouvée
    
    return answers




