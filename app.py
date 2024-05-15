from flask import Flask, request, jsonify
from services import CurrencyConverter
from utils import log_error

app = Flask(__name__)


def validate_parameters(params):
    """Проверка необходимых параметров."""
    missing_params = [param for param in params if not request.args.get(param)]
    if missing_params:
        return False, f'Пропущен обязательный параметр: {", ".join(missing_params)}'
    return True, ''


@app.route('/api/rates', methods=['GET'])
def get_conversion():
    """Ручка API для обработки запросов на конвертацию валют."""
    required_params = ['from', 'to', 'value']
    is_valid, error_message = validate_parameters(required_params)

    if not is_valid:
        return jsonify({'error': error_message}), 400

    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    try:
        amount = float(request.args.get('value'))
    except (TypeError, ValueError):
        log_error(f'Неверная или недостающая сумма для конвертации: {request.args.get("value")}')
        return jsonify({'error': 'Неверная или недостающая сумма'}), 400

    result, error = CurrencyConverter.convert(from_currency, to_currency, amount)
    if error:
        log_error(f'Ошибка конвертации из {from_currency} в {to_currency}: {error}')
        return jsonify({'error': error}), 400

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False)
