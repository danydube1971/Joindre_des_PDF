# Joindre_des_PDF

Ce script utilise les modules os et fitz pour fusionner tous les fichiers PDF dans le répertoire courant. 
Voici ce que fait chaque étape du script :

1. Utilise la fonction os.listdir() pour récupérer la liste de tous les fichiers dans le répertoire courant 
et filtre les fichiers qui ont l'extension .pdf en utilisant une compréhension de liste.
2. Trie les noms de fichiers récupérés en ordre alphabétique en utilisant la méthode .sort() de la liste pdf_files.
3. Crée un objet PdfFileMerger vide en utilisant la méthode .open() de fitz.
4. Ajoute chaque fichier PDF de la liste pdf_files à l'objet PdfFileMerger en utilisant la méthode .insert_pdf() de fitz.
5. Enregistre le fichier PDF final en utilisant la méthode .save() de l'objet PdfFileMerger et en lui donnant un nom se terminant par .join.
6. Affiche un message indiquant que la fusion des fichiers PDF est terminée.

Ainsi, à la fin de l'exécution du script, tous les fichiers PDF dans le répertoire courant auront été fusionnés en un seul fichier PDF 
nommé "output.join.pdf".

# Comment utiliser ce script

Placez le script dans le même répertoire que les fichiers PDF que vous voulez joindre.

Exécutez le script dans un terminal avec la commande suivante :

**python3 "Joindre des PDF.py"**

Testé dans Linux Mint 21

