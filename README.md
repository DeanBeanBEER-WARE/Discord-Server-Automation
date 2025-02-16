# Discord Bot Automation

Ein Python-Bot zur automatischen Verwaltung von Discord-Server-Strukturen.

## Installation

1. Erstelle eine virtuelle Umgebung:
```bash
cd /Users/denniswiebler/Documents/VSC/Discord-Bot-Automation
python3 -m venv venv
source venv/bin/activate
```

2. Installiere die erforderlichen Pakete:
```bash
pip install -r requirements.txt
```

## Einrichtung

1. Erstelle einen Discord-Bot:
   - Gehe zu [Discord Developer Portal](https://discord.com/developers/applications)
   - Klicke auf "New Application"
   - Gehe zum "Bot" Bereich
   - Aktiviere alle "Privileged Gateway Intents"
   - Kopiere den Bot-Token

2. Konfiguriere den Bot:
```bash
python src/setup.py
```
Füge deinen Bot-Token ein, wenn du dazu aufgefordert wirst.

3. Lade den Bot in deinen Server ein:
   - Gehe im Developer Portal zu "OAuth2" -> "URL Generator"
   - Wähle die Scopes: "bot" und "applications.commands"
   - Bei Bot Permissions wähle "Administrator"
   - Öffne die generierte URL im Browser
   - Wähle deinen Server aus

## Verwendung

1. Starte den Bot:
```bash
python src/discord_bot.py
```

2. Folge den Anweisungen:
   - Gib den gewünschten Server-Namen ein
   - Bestätige die Änderungen

Der Bot wird dann:
- Den Server-Namen aktualisieren
- Alle existierenden Kanäle löschen
- Neue Kategorien und Kanäle erstellen basierend auf der Template-Datei

## Anpassung der Server-Struktur

Die Server-Struktur ist in `src/templates/server_template.json` definiert. Du kannst diese Datei bearbeiten, um die Kategorien und Kanäle anzupassen.

## Projektstruktur

```
Discord-Bot-Automation/
├── README.md
├── requirements.txt
├── src/
│   ├── config/
│   │   └── .env
│   ├── templates/
│   │   └── server_template.json
│   ├── discord_bot.py
│   └── setup.py
└── venv/
```

## Sicherheitshinweise

- Teile niemals deinen Bot-Token
- Der Bot-Token wird sicher in der .env-Datei gespeichert
- Stelle sicher, dass der Bot Administrator-Rechte hat
- Beachte das Discord-Limit von 10 Server-Erstellungen pro Tag
