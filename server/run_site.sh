cd ~/virks-spellbook/server
waitress-serve --port=7777 --call "spellcard:create_app"
