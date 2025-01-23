def calculate_audit_price(sales_volume, activity_type, employees):
    base_price = 1000  # Preț de bază
    multiplier = {
        'servicii': 1.0,
        'producere': 1.5,
        'comert': 1.2,
        'ong': 0.8,
        'agricultura': 1.1,
        'constructii': 1.3,
        'transport': 1.4,
    }.get(activity_type, 1.0)

    # Formula de calcul: (bazată pe volum + număr de angajați) x multiplicator
    price = base_price + (sales_volume * 500) + (employees * 100)
    return price * multiplier
