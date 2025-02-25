from flask import * 
from public import public
from admin import admin


app=Flask(__name__)

app.secret_key="key"


app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')


app.run(debug=True,port=5081,host="0.0.0.0")