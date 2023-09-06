def val_rut(rut):
    """
    Verifica el formato y el dígito verificador de un RUT
    
    Parámetros
    ----------
    rut : str
    El número de RUT a verficiar
    
    Retorna
    ----------
    True: El RUT es válido
    False: El RUT no es válido
    None: El formato del RUT es erroneo
    """
    formato1 = "xx.xxx.xxx-x"  # len 12 / punto en [2] - [6] / guión en [10]
    formato2 = "x.xxx.xxx-x"  # len 11 / punto en [1] - [5] / guión en [9]

    # Verificamos que la entrada no sea un int
    if type(rut) == int:
        
        print('ERROR: Rut en formato incorrecto')
        return None
    
    # Verficamos que el rut sea un sting y el último valor es un número o 'k' o 'K'
    elif type(rut) == str and rut[-1].isnumeric() == True or rut[-1] == 'k' or rut[-1] == 'K':
        
        
        # FORMATO 1
        
        # Verificar que el rut (desde el inicio hasta antes del dígito verificaor) no tenga letras
        if len(rut) == len(formato1):
            rut_verificar = rut[0:2] + rut[3:6] + rut[7:10]
            if rut_verificar.isnumeric() == False:
                print("ERROR: Rut Inválido")
                return None

            # Verificamos que el RUT tiene el formato correcto con los puntos y el guion en la posicion correcta
            if rut[2] == '.' and rut[6] == '.' and rut[10] == '-':
                
                # Realizamos los calculos correspondientes para calcular el que deberia, ser el dígito verificador
                rut_verificar_inv = list(reversed(rut_verificar))
                mult = [2, 3, 4, 5, 6, 7]
                contador = 0
                resultado = 0
                for num in rut_verificar_inv:
                    resultado += int(num) * mult[contador]
                    contador += 1
                    if contador == 6:
                        contador = 0

                resto = resultado % 11
                resta = 11 - resto

                verificador = ''

                # Agregar las excepciones y verificar el rut
                if resta == 10:
                    verificador = 'K'
                elif resta == 11:
                    verificador = 0
                else:
                    verificador = resta

                rut_verificador = rut[-1]

                if rut_verificador == 'k' or rut_verificador == 'K':
                    rut_verificador = 'K'
                    if rut_verificador == verificador:
                        return True
                    return False

                elif int(rut_verificador) == verificador:
                    return True

                elif int(rut_verificador) != verificador:
                    return False

            else:
                print("ERROR: Rut Inválido")
                return None

        # FORMATO 2
        
        # Verificar que el rut (desde el inicio hasta antes del dígito verificaor) no tenga letras
        elif len(rut) == len(formato2):
            rut_verificar = rut[0] + rut[2:5] + rut[6:9]
            if rut_verificar.isnumeric() == False:
                print("ERROR: Rut Inválido")
                return None

            # Verificamos que el RUT tiene el formato correcto con los puntos y el guion en la posicion correcta
            if rut[1] == '.' and rut[5] == '.' and rut[9] == '-':
                
                # Realizamos los calculos correspondientes para calcular el que deberia, ser el dígito verificador
                rut_verificar_inv = list(reversed(rut_verificar))
                mult = [2, 3, 4, 5, 6, 7]
                contador = 0
                resultado = 0
                for num in rut_verificar_inv:
                    resultado += int(num) * mult[contador]
                    contador += 1
                    if contador == 6:
                        contador = 0

                resto = resultado % 11
                resta = 11 - resto

                verificador = ''

                # Agregar las excepciones y verificar el rut
                if resta == 10:
                    verificador = 'K'
                elif resta == 11:
                    verificador = 0
                else:
                    verificador = resta

                rut_verificador = rut[-1]

                if rut_verificador == 'k' or rut_verificador == 'K':
                    rut_verificador = 'K'
                    if rut_verificador == verificador:
                        return True
                    return False

                elif int(rut_verificador) == verificador:
                    return True

                elif int(rut_verificador) != verificador:
                    return False

            else:
                print("ERROR: Rut Inválido")
                return None

        # NINGUNO DE LOS FORMATOS ANTERIORES
        else:
            print("ERROR: Rut Inválido")
            return None
    
    # Si el valor ingresado no es válido
    else:
        print("ERROR: Rut Inválido")
        return None
