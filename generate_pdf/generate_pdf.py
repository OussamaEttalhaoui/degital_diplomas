from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_pdf_with_tx_id(name, first_name, cne, cin, degree, specialization, university, year, mention, tx_id, output_path="diplome_with_tx_id.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  

    title = f"Informations du diplôme de {first_name} {name}"
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.darkblue)
    c.drawCentredString(width / 2, height - 50, title)

    # Ligne de séparation sous le titre
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(1.5)
    c.line(50, height - 60, width - 50, height - 60)

    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)

    # Définir les positions de départ
    x_start = 100
    y_start = height - 100
    line_spacing = 20

    # Ajouter les informations détaillées dans un format structuré
    info_pairs = [
        ("Nom", name),
        ("Prénom", first_name),
        ("CNE", cne),
        ("CIN", cin),
        ("Diplôme", degree),
        ("Spécialisation", specialization),
        ("Université", university),
        ("Année d'obtention", year),
        ("Mention", mention),
        ("ID de la transaction", tx_id)
    ]

    for label, value in info_pairs:
        c.drawString(x_start, y_start, f"{label} : {value}")
        y_start -= line_spacing

    # Ajouter un pied de page avec des informations supplémentaires
    footer_text = "Ce document a été généré automatiquement et contient des informations vérifiées."
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.grey)
    c.drawCentredString(width / 2, 30, footer_text)

    # Sauvegarder le PDF
    c.save()
