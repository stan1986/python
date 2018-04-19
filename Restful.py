from flask import Flask,jsonify


app = Flask(__name__)
stores=[

    {
        "name":"my store",
        "item":[
            {"name":"My Item",
              "price":15.99
            }
            
        ]
    }
]

#Post/store data: name{}

@app.route('/store',methods=['POST'])

def create_store():

    pass


#GET /store/<string:name>

@app.route('/store/<string:name>')

def get_store():

    pass

#GET /store/

@app.route('/store')

def get_stores():

    return jsonify ({"stores":stores})

#POST /store/<string:name>/item{name:,price:}

@app.route('/store/<string:name>/item',methods=['POST'])

def create_item_in_store():

    pass

#GET/store/<string:name>/item

@app.route('/store/<string:name>/item')

def get_item_in_store():

    pass

app.run(port = 5000)
