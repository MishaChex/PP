from flask import Flask
from flask_restful import Api


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controler import *

app = Flask(__name__)
api = Api(app)

engine = create_engine('postgresql://olex:1111@localhost:5433/mydb', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    api.add_resource(AddUser, '/user')
    api.add_resource(GetUser, '/user/<int:id>')
    api.add_resource(UpdateUser, '/user/<int:id>')

    api.add_resource(AddPharmacy, '/pharmacy')
    api.add_resource(GetPharmacy, '/pharmacy/<int:id>')

    api.add_resource(AddMedicine, '/medicine/<int:pharmacy_id>')
    api.add_resource(GetMedicine, '/medicine/<int:medicine_id>')

    app.run(debug=True)




    """
    {
   "name":"Vovik",
   "login":"gtfobae",
   "phone":"09348124",
   "email":"lol@gmail.com",
   "password":"123"
    }
    """

    """
    {
   "name":"D.S.",
   "branch":"D.S.inc",
   "phone":"0943567",
   "email":"D.s.@gmail.com",
   "address":"st.Str 21b"
}
    """
    """
    {
   "name":"Farmadol",
   "description":"good",
   "category":"painkiller",
   "email":"D.s.@gmail.com"
}

    """