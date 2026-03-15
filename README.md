# 🕵️ PyDirScanner
**Scanner de répertoires web et énumérateur de chemins cachés.**

---

## ⚠️ Avertissement Légal
L'utilisation de PyDirScanner doit s'inscrire strictement dans un cadre légal (audit de sécurité autorisé, CTF, machines virtuelles privées). Ce script est conçu à des fins éducatives. L'utilisateur assume l'entière responsabilité de ses actes. Les attaques sur des systèmes tiers sans autorisation sont illégales.

## 📋 Description du Projet
PyDirScanner est un outil de reconnaissance réseau (Red Team) développé en Python. Il a pour but d'automatiser la phase de découverte d'applications web en identifiant des répertoires ou fichiers sensibles non référencés publiquement (ex: `/admin`, `/backup`, `/api`).

Ce projet permet d'appréhender le fonctionnement des requêtes HTTP et de comprendre comment un attaquant (ou un auditeur) cartographie une surface d'attaque web de manière automatisée.

## 📂 Architecture Technique
```text
PyDirScanner/
│
├── scanner.py          # Moteur de requêtes et logique de scan
└── README.md           # Documentation d'utilisation
```

## 🛠️ Mécanismes Techniques

### Phase de Reconnaissance HTTP
* **Objectif :** Valider l'existence d'une ressource web de manière programmatique.
* **Concept :** Envoi massif de requêtes vers des chemins potentiels (issus d'un dictionnaire) et analyse de la réponse du serveur cible.

### Bibliothèque Clé
* **`requests` (Tierce partie) :** 
  * **Pourquoi l'utiliser ?** Elle abstrait la complexité des requêtes HTTP brutes (sockets). Plutôt que de forger manuellement les en-têtes (Headers), `requests` gère nativement le routage, les redirections, et l'analyse du code statut de réponse HTTP (ex: `200 OK`, `404 Not Found`, `403 Forbidden`).

## 🚀 Installation & Utilisation

### Prérequis
- Système d'exploitation : Linux, macOS ou Windows.
- Langage : Python 3.8+.
- Bonne pratique : L'utilisation d'un environnement virtuel (`venv`) est recommandée.

### Déploiement

1. Cloner le dépôt localement :
   ```bash
   git clone https://github.com/VOTRE_PSEUDO/PyDirScanner.git
   cd PyDirScanner
   ```

2. (Optionnel mais recommandé) Créer et activer un environnement virtuel :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installer les dépendances :
   ```bash
   pip install requests
   ```

3. Lancer le scanner en précisant l'URL cible (`-u`) et le fichier contenant les mots à tester (`-w`) :
   ```bash
   # Demander l'aide interactive
   python3 scanner.py -h
   
   # Lancer un scan
   python3 scanner.py -u http://example.com -w dictionnaire.txt
   ```

## 🧠 Apports Pédagogiques (Niveau Intermédiaire)
- **Interface Pro (CLI) :** Utilisation de `argparse` pour forcer la standardisation de l'outil vis-à-vis des autres outils sous Kali Linux.
- **Requêtes HTTP Optimisées :** Compréhension des Timeouts et de la gestion des erreurs réseau en Python.
- **Automatisation via Listes :** Les pirates ne pensent pas "un par un", ils automatisent. Lecture dynamique de fichiers texte (Wordlists) et boucles (loops).
