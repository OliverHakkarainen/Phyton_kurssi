while True:
    try:
        tuuma = float(input("anna tuumat"))
        if tuuma <= 0:
            print("ohjelma lopetetaan")
            break

        cm = tuuma * 2.54
        print(f"{tuuma} tuuumaa on {cm} cm")
    except ValueError:
        print("anna numero")