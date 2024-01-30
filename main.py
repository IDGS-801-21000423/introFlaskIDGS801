from flask import Flask, render_template, request     #Importar flask, render template
import forms                # Importar archivo forms
app = Flask(__name__)       # Nombrar la app Flask

# Definir rutas
@app.route("/")         
def index():
  return render_template("index.html") #pagina1



@app.route("/alumnos", methods = ['GET', 'POST'])         
def alumnos():
  alumno_clase = forms.UserForm(request.form)
  if request.method == 'POST':
    pass
  
  return render_template("alumnos.html", form = alumno_clase)
  """ titulo ="UTL"
  nombres = ["mario", "pedro", "juan", "dario"] 
  return render_template("alumnos.html", titulo = titulo, nombres = nombres)"""



@app.route("/maestros")         
def mestros():
  return render_template("maestros.html") #pagina3

@app.route("/hola")
def hola():
  return "<h1>Saludos desde Hola</h1>"

@app.route("/Saludo")
def saludo():
  return "<h1>Saludos desde Saludo</h1>"



@app.route("/nombre/<string:nom>")  # Le pasamos la ruta / el tipo de parametro / y la variable
def nombre(nom):                    #Pasamos el parametro a la funcion
  return "Hola: " +nom

@app.route("/numero/<int:n1>")
def numero(n1):
  return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nom>")
def func(id, nom):
  return "ID: {} Nombre: {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1, n2):
  return "La suma {} + {} ={}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:a>")
def func3(a ="Angel"):                    # Valor por defecto en la ruta
  return "El nombre de User es: " +a

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
  if request.method == "POST":
    num1 =request.form.get("n1")
    num2 =request.form.get("n2")
    return"La multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
  else:
    return '''
    <form action="/calcular" method="POST">
      <label>N1:</label>
      <input type="text" name="n1"><br>
      <label>N2:</label>
      <input type="text" name="n2"><br>
      <input type="submit"/>
    </form>
    '''

@app.route("/OperasBas")
def operas():
  return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
  if request.method == "POST":
    num1 =request.form.get("n1")
    num2 =request.form.get("n2")
    return"La multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))



if __name__ =="__main__":
  app.run(debug=True)   # Cambios en tiempo real