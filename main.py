from app.pokemon import get_pokemon_of_the_day

pokemon = get_pokemon_of_the_day()

from flask import Flask, jsonify, render_template
from app.pokemon import get_pokemon_of_the_day

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pokemon.html")

@app.route("/api/pokemon-of-the-day")
def pokemon_of_the_day():
    pokemon = get_pokemon_of_the_day()
    return jsonify(pokemon)

if __name__ == "__main__":
    app.run(debug=True)