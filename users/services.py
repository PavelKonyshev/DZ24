import stripe
from config import settings


stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(obj):
    """Создаем stripe продукт"""

    title_product = obj.course_paid if obj.course_paid else obj.lesson_paid
    stripe_product = stripe.Product.create(name=title_product)
    return stripe_product.id


def create_stripe_price(product_id, amount):
    """ Создает цену в stripe """

    return stripe.Price.create(
        product=product_id,
        currency="rub",
        unit_amount=int(amount)*100,
    )


def create_stripe_session(price):
    """ Создает сессию и оплату в Stripe """

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')