import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomweb.settings")

import django
django.setup()

#  import your models
from shop.models import Product

def create_products():
    products = [
        {
            'name': 'Bose QuietComfort 35 II',
            'description': 'Description: The Bose QuietComfort 35 II headphones offer top-tier noise cancellation, excellent sound quality, and comfortable design for long listening sessions.',
            'price': 299.99,
            'image': 'images/Bose QuietComfort 35 II.jpg'       
        },
        {
            'name': 'Sony WH-1000XM4',
            'description': 'Description: Sony WH-1000XM4 headphones deliver exceptional noise cancellation, impressive audio performance, and long battery life, making them ideal for travelers and music enthusiasts.',
            'price': 349.99,
            'image': 'images/Sony WH-1000XM4.png'
        },
        {
            'name': 'Sennheiser HD 800 S',
            'description': 'Description: The Sennheiser HD 800 S headphones offer high-resolution sound, wide soundstage, and premium build quality, making them a favorite among audiophiles and professionals.',
            'price': 1699.99,
            'image': 'images/Sennheiser HD 800 S.jpg'
        },
        {
            'name': 'Audio-Technica ATH-M50x',
            'description': 'Description: The Audio-Technica ATH-M50x headphones provide exceptional audio clarity, deep bass response, and comfortable design, perfect for studio monitoring and critical listening.',
            'price': 149.99,
            'image': 'images/Audio-Technica ATH-M50x.jpeg'
        },
        {
            'name': 'Beats Studio3 Wireless',
            'description': 'Description: Beats Studio3 Wireless headphones feature Pure Adaptive Noise Cancelling technology, real-time audio calibration, and up to 22 hours of battery life, offering an immersive listening experience.',
            'price': 349.99,
            'image': 'images/Beats Studio3 Wireless.jpeg'
        },
        {
            'name': 'Bowers & Wilkins PX7',
            'description': 'Description: Bowers & Wilkins PX7 headphones deliver powerful, balanced sound, adaptive noise cancellation, and ergonomic design for long-lasting comfort, suitable for everyday use and travel.',
            'price': 399.99,
            'image': 'images/Bowers & Wilkins PX7.jpg'
        },
        {
            'name': 'JBL Tune 750BTNC',
            'description': 'Description: JBL Tune 750BTNC headphones provide active noise cancellation, deep bass, and hands-free calls, offering a versatile and affordable option for music lovers on the go.',
            'price': 129.99,
            'image': 'images/JBL Tune 750BTNC.jpg'
        },
        {
            'name': 'Skullcandy Crusher Wireless',
            'description': 'Description: Skullcandy Crusher Wireless headphones feature adjustable bass, Bluetooth connectivity, and long battery life, delivering immersive sound with powerful bass for music enthusiasts.',
            'price': 149.99,
            'image': 'images/Skullcandy Crusher Wireless.jpeg'
        },
        {
            'name': 'Beyerdynamic DT 770 Pro',
            'description': 'Description: The Beyerdynamic DT 770 Pro headphones offer studio-quality sound reproduction, comfortable closed-back design, and durable construction, making them suitable for professional monitoring and mixing.',
            'price': 179.99,
            'image': 'images/Beyerdynamic DT 770 Pro.jpg'
        },
        {
            'name': 'AKG K702',
            'description': 'Description: The AKG K702 headphones feature open-back design, reference-quality sound, and comfortable fit, ideal for critical listening, mixing, and mastering applications in professional studios.',
            'price': 349.99,
            'image': 'images/AKG K702.jpg'
        }
]

    

    for product_data in products:
        Product.objects.create(**product_data)

create_products()
