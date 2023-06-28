unidades = {"m": "m->cm", "kg": "kg->g", "l": "L->mL", "h": "h->min", "c": "°C->°F", "m2": "m2->ft2",
            "kmh": "km/h->m/s", "t": "t->kg", "l100": "L/100km->gal/mi", "usd": "USD->Euro"}


def menu(unidades):
    i = 1
    for opcion, unidad in unidades.items():
        print(f"{i}. {unidad} | Opc: {opcion}")
        i += 1
    return unidades


def metro_cm(unidad):
    resultado = unidad * 100
    return f"{unidad}m son {resultado}cm"


def kilogramo_gm(unidad):
    resultado = unidad * 1000
    return f"{unidad}kg son {resultado}g"


def litro_ml(unidad):
    resultado = unidad * 100
    return f"{unidad}L son {resultado}mL"


def hora_m(unidad):
    resultado = unidad * 60
    return f"{unidad}h son {resultado}min"


def gradoc_f(unidad):
    resultado = unidad * (9/5) + 32
    return f"{unidad}°C son {resultado}°F"
