#!/usr/bin/env python3

"""Ce script utilise la bibliothèque PyMuPDF pour fusionner les fichiers PDF dans le répertoire courant. 
Les fichiers PDF sont triés par ordre alphabétique avant d'être fusionnés. 
Il faut installer le module PyMuPDF avec la commande pip3 install PyMuPDF"""

import os
import fitz

# Récupérer tous les fichiers PDF dans le répertoire courant
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

# Trier les fichiers PDF par ordre alphabétique
pdf_files.sort()

# Créer un objet PdfFileMerger pour fusionner les fichiers PDF
pdf_merger = fitz.open()

# Ajouter chaque fichier PDF à l'objet PdfFileMerger
for filename in pdf_files:
    with fitz.open(filename) as pdf_file:
        pdf_merger.insert_pdf(pdf_file)

# Écrire le fichier PDF final avec un nom se terminant par .join
pdf_merger.save("output.join.pdf")

print("Fusion des fichiers PDF terminée.")

