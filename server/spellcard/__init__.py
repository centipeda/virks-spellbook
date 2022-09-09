
from flask import Flask, request, make_response
import os
import tempfile

import spell.cards
import spell.info

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/spellcard')
    def spellcard():
        if request.args.get("cards") is None:
            return "missing cards param", 400
        
        try:
            card_ids = [int(x) for x in request.args.get("cards").split(",")]
        except Exception as e:
            print(e)
            return "bad cards param", 400
        
        file = tempfile.NamedTemporaryFile(suffix=".pdf")

        cards = []
        for card_id in card_ids:
            card_info = spell.info.find_spell("id", card_id)
            if card_info is None:
                return "bad spell id", 400
            cards.extend(spell.cards.gen_cards(card_info))

        print(len(cards))
        spell.cards.make_printable(cards, file)

        file.seek(0)
        binary_pdf = file.read()

        response = make_response(binary_pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response


    return app