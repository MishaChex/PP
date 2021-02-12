from models import Pharmacy, User, Medicine,create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://olex:1111@localhost:5433/mydb", echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

session = Session()

user1 = User(id=1, name='Nazar', phone='+380675617204', mail='lol@gmail.com', password='1111')
user2 = User(id=2, name='Vova', phone='+380500666028', mail='kek@gmail.com', password='2222')

pharmacy1 = Pharmacy(id=1, name='DS', phone='2388908', branch='D.S.', mail='D.S.Str@gmail.com', address='st.Str 21b')
pharmacy2 = Pharmacy(id=2, name='ZI', phone='2388593', branch='Apteka ZI', mail='ZI.Yar@gmail.com', address='st.Yar')
pharmacy3 = Pharmacy(id=3, name='Znahar', phone='2384557', branch='Znahar', mail='Znahar.Zub@gmail.com', address='Zub')

medicine1 = Medicine(id=1, name='Farmadol', description='Good medicine', category='painkiller', pharmacy_id=1)
medicine2 = Medicine(id=2, name='Korvalol', description='Good medicine', category='heart', pharmacy_id=3)
medicine3 = Medicine(id=3, name='Enap-H', description='Good medicine', category='hormonal', pharmacy_id=2)
medicine4 = Medicine(id=4, name='Validol', description='Good medicine', category='heart', pharmacy_id=1)
medicine5 = Medicine(id=5, name='Aspirin', description='Good medicine', category='oilol', pharmacy_id=3)

session.add(user1)
session.commit()

session.add(user2)
session.commit()

session.add(pharmacy1)
session.commit()

session.add(pharmacy2)
session.commit()

session.add(pharmacy3)
session.commit()

session.add(medicine1)
session.commit()

session.add(medicine2)
session.commit()

session.add(medicine3)
session.commit()

session.add(medicine4)
session.commit()

session.add(medicine5)
session.commit()

session.close()