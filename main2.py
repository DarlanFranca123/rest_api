from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Base de Dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///candidatos.db"

db = SQLAlchemy(app)

class Candidatos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    semestre = db.Column(db.Integer, nullable = False)
    ira = db.Column(db.Float, nullable = False)

    def to_dict(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "semestre" : self.semestre,
            "ira" : self.ira
        }

with app.app_context():
    db.create_all()

#Routes

@app.route("/")
def home():
    return jsonify({"mensagem" : "voce esta na pagina principal"})

@app.route("/candidatos", methods = ["GET"])
def todos_candidatos():
    all_candidatos = Candidatos.query.all()
    return jsonify([candidato.to_dict() for candidato in all_candidatos])

@app.route("/candidatos/<int:candidato_id>", methods = ["GET"])
def candidato_by_id(candidato_id):
    candidato = Candidatos.query.get(candidato_id)
    if candidato: 
        return jsonify(candidato.to_dict())
    else:
        return jsonify({"erro": "candidato nao encontrado"}), 404

#POST 

@app.route("/candidatos", methods = ["POST"])
def inserir_candidato():
    dados = request.get_json()

    novo_candidato = Candidatos(nome = dados["nome"], 
                                semestre = dados["semestre"], 
                                ira = dados["ira"])
    db.session.add(novo_candidato)
    db.session.commit()
    return jsonify(novo_candidato.to_dict())

#PUT
@app.route("/candidatos/<int:candidato_id>", methods = ["PUT"])
def trocar_candidato_by_id(candidato_id):
    dados_candidato_novo = request.get_json()

    candidato = Candidatos.query.get(candidato_id)
    if candidato: 
        candidato.nome = dados_candidato_novo.get("nome",candidato.nome)
        candidato.semestre = dados_candidato_novo.get("semestre",candidato.semestre)
        candidato.ira = dados_candidato_novo.get("ira",candidato.ira)

        db.session.commit()
        return jsonify(candidato.to_dict())
    else:
        jsonify({"erro": "candidato nao encontrado"})

#DELETE
@app.route("/candidatos/<int:candidato_id>", methods = ["DELETE"])
def deletar_candidato_by_id(candidato_id):
    candidato = Candidatos.query.get(candidato_id)
    if candidato:
        db.session.delete(candidato)
        db.session.commit()
        return jsonify({"mensagem" : "candidato deletado"})
    else: 
        return jsonify({"erro": "candidato nao encontrado"})


if __name__ == "__main__":
    app.run(debug=True)
