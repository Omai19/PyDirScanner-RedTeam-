import requests
import argparse
import sys
import time

def print_banner():
    print("""
=================================================
       🕵️  PyDirScanner V1.5 (Pro Edition)
=================================================
    """)

def scanner_repertoire(url_cible, chemin_wordlist):
    """
    Lit une wordlist et teste chaque répertoire sur le serveur cible.
    """
    # Nettoyage de l'URL cible (s'assurer qu'elle se termine par une barre oblique '/')
    if not url_cible.endswith('/'):
        url_cible += '/'

    print(f"[*] Cible     : {url_cible}")
    print(f"[*] Wordlist  : {chemin_wordlist}")
    print("-" * 50)
    
    repertoires_trouves = []
    
    try:
        # Ouverture du fichier dictionnaire
        with open(chemin_wordlist, 'r', encoding='utf-8', errors='ignore') as fichier:
            lignes = fichier.readlines()
            total_mots = len(lignes)
            
            print(f"[*] {total_mots} chemins chargés. Démarrage du scan...\n")
            
            for index, ligne in enumerate(lignes, 1):
                mot = ligne.strip()
                if not mot:
                    continue # Ignorer les lignes vides
                
                url_complete = url_cible + mot
                
                # Feedback visuel dans le terminal (pour voir que ça tourne)
                # end='\r' permet de réécrire sur la même ligne
                sys.stdout.write(f"\r[~] Test [{index}/{total_mots}] : {url_complete} ")
                sys.stdout.flush()
                
                try:
                    # Envoi de la requête (timeout de 3 secondes pour ne pas bloquer)
                    reponse = requests.get(url_complete, timeout=3)
                    
                    # Si la page répond 200 (OK) ou 403 (Interdit, mais existe)
                    if reponse.status_code in [200, 403]:
                        # On efface la ligne d'attente
                        sys.stdout.write('\r' + ' ' * 60 + '\r')
                        
                        if reponse.status_code == 200:
                            statut = "🟢 200 OK"
                        else:
                            statut = "🟠 403 FORBIDDEN"
                            
                        print(f"[+] TROUVÉ [{statut}] : /{mot}")
                        repertoires_trouves.append(f"/{mot} (Code {reponse.status_code})")
                        
                except requests.exceptions.RequestException:
                    pass # Si un timeout se produit sur un chemin spécifique, on passe au suivant
                
                # Petite pause pour ne pas surcharger le serveur et simuler un comportement humain
                time.sleep(0.1)
                
    except FileNotFoundError:
        print(f"\n[-] ERREUR FATALE : Le fichier '{chemin_wordlist}' n'existe pas.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] ERREUR FATALE inattendue : {str(e)}")
        sys.exit(1)

    # Affichage du rapport final
    sys.stdout.write('\r' + ' ' * 60 + '\r') # Nettoyage de la dernière ligne
    print("-" * 50)
    print("📋 RAPPORT DE SCAN")
    print("-" * 50)
    if repertoires_trouves:
        for rep in repertoires_trouves:
            print(f"  👉 {rep}")
    else:
        print("  ❌ Aucun répertoire caché n'a été trouvé.")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Énumérateur de répertoires web par force brute (Reconnaissance).")
    
    parser.add_argument("-u", "--url", required=True, help="L'URL de base à scanner (ex: http://192.168.1.10/).")
    parser.add_argument("-w", "--wordlist", required=True, help="Chemin vers le dictionnaire de dossiers (ex: common.txt).")
    
    args = parser.parse_args()
    
    # Validation du format de l'URL brute
    if not (args.url.startswith("http://") or args.url.startswith("https://")):
        print("[-] ERREUR : L'URL doit commencer par 'http://' ou 'https://'.")
        sys.exit(1)
        
    scanner_repertoire(args.url, args.wordlist)

if __name__ == "__main__":
    main()
