from flask import Flask, request, jsonify
from janome.tokenizer import Tokenizer
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

T = Tokenizer()

def AnalyzeJaome(Msm):
  Tokens = T.tokenize(Msm)

  DataArray = []
  tmpTokenArray = {}
  for Token in Tokens:
    tmpTokenArray["surface"] = Token.surface
    tmpTokenArray["part"] = Token.part_of_speech.split(',')[0]
    print(tmpTokenArray)
    DataArray.append(tmpTokenArray.copy())

  return DataArray



@app.route('/', methods=['POST', 'GET'])
def post_reqest():
  if request.method == 'POST':
    if "msg" in request.form:
      State = "OK"
      Msg = AnalyzeJaome( request.form['msg'] )

    else:
      State = "NG #2"
      Msg = "not suport arg"

  else:
    State = "NG #1"
    Msg = "not support method"

  return  jsonify({ 'status':State, 'result':Msg })



if __name__ == '__main__':
  app.run()
