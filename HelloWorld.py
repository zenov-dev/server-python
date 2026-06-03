def besked(navn):
    """
    Returnerer en Hello World besked.

    Args:
        navn (str): Navnet på personen.

    Returns:
        str: En hilsen.
    """
    return f"Hello World, {navn}"


navne = ["Anders", "Mette", "Peter"]

for navn in navne:
    if navn == "Anders":
        print(besked(navn))
    elif navn == "Mette":
        print(besked(navn))
    else:
        print(f"Hello World, ukendt bruger: {navn}")