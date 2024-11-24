from flask import Flask, jsonify
import pandas as pd 
app = Flask(__name__)

@app.route('/dados')

def site():  
    info = pd.read_csv('../1_Bases_Tratadas/MagazineTratada.csv')

    media_preco = info['Preços'].mean()
    media = {'Media dos precos dos celulares: R$': media_preco}
    
    mediana_preco = info['Preços'].median()
    mediana = {'mediana dos Precos dos celulares: R$': mediana_preco}
     
    dp_preco = info ['Preços'].std()
    dp = {'Desvio padrao dos precos: R$': dp_preco}
    
    resposta = {'mediaprecoscelulares': media_preco, 'medianaprecoscelulares': mediana_preco, 'Desviopadraoprecos': dp_preco}
    return jsonify(resposta)

      
app.run(debug = True)
