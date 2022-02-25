from classes import Model


async def get_history(model: Model, market: str) -> str:
    text = [f"История изменения цен <b>{model.name}</b> в <b>{market}</b>\n"]

    history = model.get_history()
    points = tuple(filter(lambda point: point.prices.get(market), history.points))
    date_format = "%d/%m/%Y %H:%M"

    text.append(f"{points[0].date.strftime(date_format)} | <b>{points[0].prices.get(market)}</b>₽")

    for points_index in range(1, len(points)):
        previous_point, current_point = points[points_index - 1], points[points_index]
        previous_price, current_price = previous_point.prices.get(market), current_point.prices.get(market)

        if not current_price or not previous_price:
            continue

        if current_price != previous_price:
            text.append(f"{current_point.date.strftime(date_format)} | <b>{current_price}</b>₽")

    return "\n".join(text)

