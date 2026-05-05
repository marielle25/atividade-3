from flask import Flask, render_template

app = Flask(__name__)

#index
@app.route('/')
def index():
    return render_template('index.html')

#questao 01
@app.route('/shakespeare/<int:idioma>')
def shakespeare(pt , en): 
    if idioma=='en': 
      return render_template("ingles.html ")
    elif idioma== 'pt':
       return render_template("portugues.html")
    else:
     return "idioma desconhecido"


if_name_ == '_main_':
   app.rum(debug=True)               
#questao 02
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/permissaoparadirigir')
def permissao():
    return render_template'permissaoparadirigir.html'

@app.route('/verificarpermissao/<int:idade>')
def verificar():
     idade = int(request.form['idade'])


  if idade >= 18: 
      mensagem = "Você ja tem permissão para dirigir"
      imagem = "dirigindo.jpg"
  else:
     mensagem = "você não tem permisão para dirigir!"
     imagem = "carona.jpg" 


 return render_template('resultado.html', mensagem=mensagem, imagem=imagem) 


if __name__== '_main_':
    app.rum(debug=True)     
#questao 03
from flask import flask, render_template, request


app = flask(__name__)


@app.route('/criarquestoes', methods=['POST'])
def criarquestoes():
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')


    lista_questoes = [q1, q2, q3]


   return render_template('criarquestoes.html', questoes=lista_questoes)


if __name__== '_main_':
    app.rum(debug=True)

#questao04
@app.route('/fazeravaliacao', methods=['GET'])
def fazeravaliacao():
  return render_template('fazeravaliacao.html')

@app.route('/recebeavaliacao', methods=['POST'])
def recebe_avaliacao():
  #receba os dados do formulário. Lembre de converter a nota para inteiro
  nome = request.form.get('nome')
  nota =int(request.form.get('rota'))
  comentario = request.form.get('comentario')

   
  return render_template(
    'recebeavaliacao.html',
     nome=nome,
     nota=nata_int,
    comentario=comentario
   )
                        
if _name_ == '_main_':
    app.run(debug=True)

#questao05
@app.route('/avaliacoes', methods=['GET'])
def exibir_avaliacoes():
    

    avaliacoes= [
        {"nome": "joão", "nota": 5,}
    ]

    return render_template('avaliacoes.html', avaliacoes_data=avaliacoes)