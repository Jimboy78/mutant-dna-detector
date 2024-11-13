from flask import Flask, request, jsonify
from app.mutant_checker import is_mutant
from app.database import store_dna, get_stats

app = Flask(__name__)


@app.route('/mutant/', methods=['POST'])
def mutant():
    data = request.get_json()
    dna = data.get('dna', [])
    if not dna or not isinstance(dna, list):
        return jsonify({"error": "Invalid DNA format"}), 400

    if is_mutant(dna):
        store_dna(dna, True)
        return jsonify({"message": "Mutant detected"}), 200
    else:
        store_dna(dna, False)
        return jsonify({"message": "Human detected"}), 403


@app.route('/stats', methods=['GET'])
def stats():
    stats_data = get_stats()
    return jsonify(stats_data), 200
