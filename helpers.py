from datetime import datetime


def _format_timestamp():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('_%Y-%m-%d-%H-%M-%S')

    return formatted_datetime


def _generate_test_data(test_data: str, date: str):
    return test_data + date


def _generate_test_email(email: str,  date: str):
    return _generate_test_data(test_data=email, date=date) + '@mail.ru'


def generate_test_data_for_product():
    """Создание тестовых данных для создания продукта."""
    test_date = _format_timestamp()
    return {
        'product_name': _generate_test_data(test_data='TestProductName', date=test_date),
        'meta_tag_title': _generate_test_data(test_data='TestMetaTagTitle', date=test_date),
        'model_name': _generate_test_data(test_data='TestModel', date=test_date),
        'keyword': _generate_test_data(test_data='product', date=test_date)
    }


def generate_test_data_for_user_registration():
    """Генерация тестовых данных для регистрации пользователя."""
    test_date = _format_timestamp()
    return {
        'first_name': _generate_test_data(test_data='TestUserName', date=test_date),
        'last_name': _generate_test_data(test_data='UserLastName', date=test_date),
        'email': _generate_test_email(email='test', date=test_date),
        'password': "testpassword"
    }
