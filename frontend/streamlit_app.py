import streamlit as st
import pandas as pd
import sys
import os

# Ajouter le répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from diplome_extraction.extract_info import extract_information_from_image,extract_information_from_pdf
from generate_pdf.generate_pdf import generate_pdf_with_tx_id
from blockchain.scripts.interact_with_blockchain import store_diploma_on_chain
from Database.store_in_mongodb import store_diploma_in_mongodb


# Configuration de Streamlit
st.set_page_config(page_title="BlockDiplomas", page_icon="🎓", layout="centered")

def main():
    # Titre principal avec icône
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>🎓 BlockDiplomas</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 16px; color: #555;'>Téléchargez un diplôme, extrayez les informations, sauvegardez-les dans la blockchain, et générez un PDF sécurisé.</p>",
        unsafe_allow_html=True
    )
    
    # Étape 1 : Téléchargement de l'image ou du pdf
    st.markdown("### Étape 1 : Téléchargez une image ou un pdf de diplôme 📄")
    uploaded_file = st.file_uploader(
        "Formats acceptés : PNG, JPG, JPEG, PDF",
        type=["png", "jpg", "jpeg", "pdf"]
    )
    
    # Si un fichier est téléchargé et si les informations n'ont pas encore été extraites
    if uploaded_file and "answers" not in st.session_state:
        # Sauvegarder le fichier téléchargé temporairement
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("✅ Fichier téléchargé avec succès !")

        # Vérifier si c'est une image ou un PDF et traiter en conséquence
        if uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
            st.markdown("### Étape 2 : Extraction des informations de l'image 🛠️")
            st.info("Veuillez patienter pendant que nous extrayons les informations...")
            answers = extract_information_from_image(file_path)
        elif uploaded_file.type == "application/pdf":
            st.markdown("### Étape 2 : Extraction des informations du PDF 🛠️")
            st.info("Veuillez patienter pendant que nous extrayons les informations...")
            answers = extract_information_from_pdf(file_path)

        if answers:
            st.session_state.answers = answers
            st.markdown("#### Informations extraites avec succès 📋")
            
            # Afficher les informations extraites sous forme de tableau
            df = pd.DataFrame(list(answers.items()), columns=["Champ", "Valeur"])
            st.dataframe(df.style.set_table_styles(
                [
                    {'selector': 'thead th', 'props': [('background-color', '#4CAF50'), ('color', 'white')]},
                    {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
                ]
            ))

    # Vérifier si des informations sont disponibles pour correction
    if "answers" in st.session_state:
        st.markdown("### Étape 3 : Corrigez les informations extraites ✏️")
        st.info("Vous pouvez modifier ou valider les informations avant de continuer.")
        
        answers = st.session_state.answers
        # Saisie des données avec session_state pour éviter de tout recharger
        nom_etudiant = st.text_input("Nom de l'étudiant", answers.get("Nom de l'étudiant", ""))
        prenom_etudiant = st.text_input("Prénom de l'étudiant", answers.get("Prénom de l'étudiant", ""))
        cne_etudiant = st.text_input("CNE de l'étudiant", answers.get("CNE de l'étudiant", ""))
        cin_etudiant = st.text_input("CIN de l'étudiant", answers.get("CIN de l'étudiant", ""))
        diplome_obtenu = st.text_input("Diplôme obtenu", answers.get("Diplôme obtenu", ""))
        specialisation_diplome = st.text_input("Spécialisation du diplôme", answers.get("Spécialisation du diplôme", ""))
        universite_obtention = st.text_input("Université d'obtention", answers.get("Université d'obtention", ""))
        annee_obtention = st.text_input("Année d'obtention", answers.get("Année d'obtention", ""))
        mention_diplome = st.text_input("Mention du diplôme", answers.get("Mention du diplôme", ""))
        
        # Créer un dictionnaire des informations corrigées
        corrected_answers = {
            "Nom de l'étudiant": nom_etudiant,
            "Prénom de l'étudiant": prenom_etudiant,
            "CNE de l'étudiant": cne_etudiant,
            "CIN de l'étudiant": cin_etudiant,
            "Diplôme obtenu": diplome_obtenu,
            "Spécialisation du diplôme": specialisation_diplome,
            "Université d'obtention": universite_obtention,
            "Année d'obtention": annee_obtention,
            "Mention du diplôme": mention_diplome
        }

        # Étape 4 : Sauvegarder dans la blockchain
        if st.button(" Enregistrer dans la Blockchain"):
            student_data = {
                'nom': corrected_answers.get("Nom de l'étudiant", ""),
                'prenom': corrected_answers.get("Prénom de l'étudiant", ""),
                'cne': corrected_answers.get("CNE de l'étudiant", ""),
                'cin': corrected_answers.get("CIN de l'étudiant", ""),
                'diplome': corrected_answers.get("Diplôme obtenu", ""),
                'specialization': corrected_answers.get("Spécialisation du diplôme", ""),
                'university': corrected_answers.get("Université d'obtention", ""),
                'year': int(corrected_answers.get("Année d'obtention", "").split("/")[1]),
                'mention': corrected_answers.get("Mention du diplôme", "Inconnue")
            }
            
            # Enregistrer dans MongoDB
            mongo_message = store_diploma_in_mongodb(corrected_answers)
            st.success(mongo_message)

            # Enregistrer dans la blockchain
            transaction_id = store_diploma_on_chain(student_data)
            st.success(f"Diplôme enregistré avec succès dans la Blockchain ! ID de la transaction : {transaction_id}")
            
            # Générer le PDF avec l'ID de la transaction
            pdf_with_tx_id_path = "diplome_with_tx_id.pdf"
            generate_pdf_with_tx_id(
                corrected_answers["Nom de l'étudiant"],
                corrected_answers["Prénom de l'étudiant"],
                corrected_answers["CNE de l'étudiant"],
                corrected_answers["CIN de l'étudiant"],
                corrected_answers["Diplôme obtenu"],
                corrected_answers["Spécialisation du diplôme"],
                corrected_answers["Université d'obtention"],
                corrected_answers["Année d'obtention"],
                corrected_answers["Mention du diplôme"],
                transaction_id,
                output_path=pdf_with_tx_id_path
            )
            with open(pdf_with_tx_id_path, "rb") as pdf_file:
                st.download_button(
                    label="📥 Télécharger le PDF avec ID de la transaction",
                    data=pdf_file,
                    file_name="diplome_with_tx_id.pdf",
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()

