from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Создание базового класса для моделей
Base = declarative_base()

# Модели для таблиц

class Courier(Base):
    __tablename__ = 'Courier'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    passport_number = Column(String)
    birth_date = Column(Date)
    hire_date = Column(Date)
    work_start_time = Column(String)
    work_end_time = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    apartment_number = Column(String)
    phone_number = Column(String)

class Transport(Base):
    __tablename__ = 'Transport'
    id = Column(Integer, primary_key=True)
    car_number = Column(String)
    brand = Column(String)
    registration_date = Column(Date)
    color = Column(String)

class Sender(Base):
    __tablename__ = 'Sender'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    birth_date = Column(Date)
    index = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    apartment_number = Column(String)
    phone_number = Column(String)

class Recipient(Base):
    __tablename__ = 'Recipient'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    birth_date = Column(Date)
    index = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    apartment_number = Column(String)
    phone_number = Column(String)

class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('Sender.id'))
    recipient_id = Column(Integer, ForeignKey('Recipient.id'))
    courier_id = Column(Integer, ForeignKey('Courier.id'))
    transport_id = Column(Integer, ForeignKey('Transport.id'))
    order_date = Column(Date)
    delivery_date = Column(Date)
    delivery_price = Column(Integer)

    sender = relationship('Sender')
    recipient = relationship('Recipient')
    courier = relationship('Courier')
    transport = relationship('Transport')

# Создаем подключение к базе данных (используем уже существующую)
engine = create_engine('sqlite:///delivery.db')

# Создаем все таблицы (если они еще не созданы)
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Создание данных для курьеров и транспорта (которые вы использовали в заказах)
courier1 = Courier(surname='Иванов', name='Иван', patronymic='Иванович', passport_number='1234567890', birth_date=date(1990, 1, 1),
                   hire_date=date(2020, 5, 1), work_start_time='08:00', work_end_time='17:00', city='Москва', street='Пушкинская',
                   house_number='12', apartment_number='2', phone_number='89101122334')
courier2 = Courier(surname='Петров', name='Петр', patronymic='Петрович', passport_number='9876543210', birth_date=date(1985, 2, 2),
                   hire_date=date(2018, 7, 15), work_start_time='09:00', work_end_time='18:00', city='Питер', street='Невский',
                   house_number='25', apartment_number='3', phone_number='89223344556')

transport1 = Transport(car_number='A123BC', brand='Toyota', registration_date=date(2020, 1, 10), color='Black')
transport2 = Transport(car_number='B456CD', brand='Ford', registration_date=date(2021, 3, 25), color='White')

# Добавление данных в таблицы Sender, Recipient, Courier, Transport
session.add_all([courier1, courier2, transport1, transport2])
session.commit()

# Данные для отправителей и получателей
sender1 = Sender(surname='Сидоров', name='Сидор', patronymic='Сидорович', birth_date=date(1975, 5, 5),
                 index='12345', city='Москва', street='Арбат', house_number='10', apartment_number='5', phone_number='89101122334')
sender2 = Sender(surname='Кузнецов', name='Кузьма', patronymic='Кузьмич', birth_date=date(1980, 6, 6),
                 index='54321', city='Питер', street='Ленинградская', house_number='20', apartment_number='10', phone_number='89223344556')

recipient1 = Recipient(surname='Петров', name='Петр', patronymic='Петрович', birth_date=date(1987, 7, 7),
                       index='10000', city='Москва', street='Тверская', house_number='30', apartment_number='15', phone_number='89112223344')
recipient2 = Recipient(surname='Иванова', name='Иванна', patronymic='Ивановна', birth_date=date(1990, 8, 8),
                       index='20000', city='Питер', street='Невский', house_number='40', apartment_number='25', phone_number='89224455677')

# Добавление данных в сессию
session.add_all([sender1, sender2, recipient1, recipient2])
session.commit()

# Данные для заказов (с использованием id, полученных после добавления данных)
order1 = Order(sender_id=sender1.id, recipient_id=recipient1.id, courier_id=courier1.id, transport_id=transport1.id,
               order_date=date(2025, 1, 1), delivery_date=date(2025, 1, 2), delivery_price=500)
order2 = Order(sender_id=sender2.id, recipient_id=recipient2.id, courier_id=courier2.id, transport_id=transport2.id,
               order_date=date(2025, 1, 3), delivery_date=date(2025, 1, 4), delivery_price=700)

session.add_all([order1, order2])
session.commit()

# Закрываем сессию
session.close()
