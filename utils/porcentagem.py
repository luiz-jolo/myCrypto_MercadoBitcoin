
def calc_porc(anterior, nova):
    anterior = anterior
    nova = nova
    x = round((nova-anterior)/anterior * 100,2)

    if anterior < nova:
        x = ("+" + str(x))
        return x

    elif anterior > nova:
        x = str(x)
        return x

    else:
        x = ("-%")
        return x