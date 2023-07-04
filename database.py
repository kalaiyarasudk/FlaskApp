from market import db
from market.models import Item, User
from market import app

# with app.app_context():
#     db.drop_all()
#     db.create_all()
    
#     # Add 10 different phone data
#     phones = [
#         {
#             'name': 'laptop',
#             'price': 1000,
#             'description': 'This is a brand new Laptop',
#             'owner' : 7
#         },
#         {
#             'name': 'Samsung Galaxy S20',
#             'price': 989,
#             'description': 'The latest Samsung flagship phone',
#             'user_id' : 8
#         },
#         {
#             'name': 'Google Pixel 7',
#             'price': 899,
#             'description': 'Google\'s new smartphone with advanced camera features',
#             'user_id' : 9
#         },
#         # Add more phones here...
#     ]
    
#     for phone in phones:
#         item = Item(name=phone['name'], price=phone['price'], description=phone['description'], owner=phone['user_id'])
#         db.session.add(item)
    
#     db.session.commit()

# from app import db
# from app.models import Item

# Create laptop data entries
# from app import db
# from app.models import Item

# Create laptop data entries
with app.app_context():
    db.drop_all()
    db.create_all()
    laptop_data = [
        {
            'name': 'Laptop 1',
            'barcode': '123456789012',
            'price': 1000,
            'description': 'Powerful laptop with high-performance specifications.',
            'owner': 1  # Assuming the owner's ID is 1
        },
        {
            'name': 'Laptop 2',
            'barcode': '234567890123',
            'price': 1500,
            'description': 'Thin and lightweight laptop for on-the-go productivity.',
            'owner': 2  # Assuming the owner's ID is 2
        },
        {
            'name': 'Laptop 3',
            'barcode': '345678901234',
            'price': 1200,
            'description': 'Gaming laptop with dedicated graphics and high-refresh-rate display.',
            'owner': 1  # Assuming the owner's ID is 1
        },
        {
            'name': 'Laptop 4',
            'barcode': '456789012345',
            'price': 900,
            'description': 'Affordable laptop with decent performance.',
            'owner': 3  # Assuming the owner's ID is 3
        },
        {
            'name': 'Laptop 5',
            'barcode': '567890123456',
            'price': 2000,
            'description': 'Premium laptop with top-of-the-line features.',
            'owner': 2  # Assuming the owner's ID is 2
        },
        {
            'name': 'Laptop 6',
            'barcode': '678901234567',
            'price': 1300,
            'description': 'Convertible laptop with touchscreen and stylus support.',
            'owner': 3  # Assuming the owner's ID is 3
        },
        {
            'name': 'Laptop 7',
            'barcode': '789012345678',
            'price': 1100,
            'description': 'Laptop for multimedia and content creation.',
            'owner': 1  # Assuming the owner's ID is 1
        },
        {
            'name': 'Laptop 8',
            'barcode': '890123456789',
            'price': 1800,
            'description': 'Laptop with long battery life and efficient performance.',
            'owner': 2  # Assuming the owner's ID is 2
        },
        {
            'name': 'Laptop 9',
            'barcode': '901234567890',
            'price': 950,
            'description': 'Budget-friendly laptop for everyday tasks.',
            'owner': 3  # Assuming the owner's ID is 3
        },
        {
            'name': 'Laptop 10',
            'barcode': '012345678901',
            'price': 1700,
            'description': 'High-resolution display and powerful graphics for gaming enthusiasts.',
            'owner': 1  # Assuming the owner's ID is 1
        },
    ]

    # Insert laptop data into the database
    for laptop in laptop_data:
        new_laptop = Item(
            name=laptop['name'],
            barcode=laptop['barcode'],
            price=laptop['price'],
            description=laptop['description'],
            owner=laptop['owner']
        )
        db.session.add(new_laptop)

    # Commit the changes to the database
    db.session.commit()
