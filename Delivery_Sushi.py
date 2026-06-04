while True:
    pikachu_roll = 0
    otaku_roll = 0
    pulpo_venenoso_roll = 0
    anguila_electrica_roll = 0

    precio_pikachu = 4500
    precio_otaku = 5000
    precio_pulpo_venenoso = 5200
    precio_anguila_electrica = 4800

    haciendo_pedido = True
    print("\n--- BIENVENIDO AL DELIVERY DE SUSHI ---")

    while haciendo_pedido:
        print("\nMenú de Rolls:")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Terminar pedido")
        opcion = input("Seleccione una opcion para agregar al pedido (1-5):")
        if opcion == '1':
            pikachu_roll += 1
            print("Pikachu Roll agregado al pedido.")
        elif opcion == '2':
            otaku_roll += 1
            print("Otaku Roll agregado al pedido.")
        elif opcion == '3':
            pulpo_venenoso_roll += 1
            print("Pulpo Venenoso Roll agregado al pedido.")
        elif opcion == '4':
            anguila_electrica_roll += 1
            print("Anguila Eléctrica Roll agregado al pedido.")
        elif opcion == '5':
            haciendo_pedido = False
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    total_productos = (
        pikachu_roll +
        otaku_roll +
        pulpo_venenoso_roll +
        anguila_electrica_roll
    )
    subtotal = (
        pikachu_roll * precio_pikachu +
        otaku_roll * precio_otaku +
        pulpo_venenoso_roll * precio_pulpo_venenoso +
        anguila_electrica_roll * precio_anguila_electrica
    )

    if total_productos > 0:
        descuento = 0
        print("\n¿tiene un codigo de descuento?")
        print("1. SI")
        print("2. No")
        opc_desc = input("Seleccione una opción (1-2):")
        if opc_desc == '1':
            while True:
                codigo = input("\nIngrese su codigo de descuento (o X para cancelar):")
                if codigo.upper() == "SOYOTAKU":
                    descuento = int(subtotal * 0.1)
                    print("¡Codigo aceptado! Se ha aplicado un 10% de descuento.")
                    break
                elif codigo.upper() == "X":
                    print("¡Cancelando ingreso de codigo de descuento. No se aplicará ningún descuento!")
                    break
                else:
                    print("Codigo no valido.")

        print("=====================================")
        print(f"TOTAL PRODUCTOS: {total_productos}")
        print("=====================================")
        print(f"CANTIDAD DE PIKACHU ROLL: {pikachu_roll}")
        print(f"CANTIDAD DE OTAKU ROLL: {otaku_roll}")
        print(f"CANTIDAD DE PULPO VENENOSO ROLL: {pulpo_venenoso_roll}")
        print(f"CANTIDAD DE ANGUILA ELECTRICA ROLL: {anguila_electrica_roll}")
        print("=====================================")
        print(f"SUBTOTAL POR PAGAR: ${subtotal}")
        print(f"DESCUENTO POR CODIGO: ${descuento}")

        total_final = subtotal - descuento
        print(f"TOTAL A PAGAR: ${total_final}")
    else:
        print("No agrego ningun producto al pedido.")
    print("=====================================")
    otro_pedido = input("¿Desea realizar otro pedido? (s/n):")
    if otro_pedido.lower() != 's':
        print("Gracias por preferir nuestros rolls de sushi. ¡Hasta pronto!")
        break