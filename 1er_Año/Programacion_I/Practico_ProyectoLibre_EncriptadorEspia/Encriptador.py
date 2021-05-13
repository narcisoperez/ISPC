#Librerias
from time import sleep
from os import system, name

#Datos del usuario
usuario = '007'
contraseña = 'bondJamesbond'

#Funciones
def limpiarTerminal():
    '''
    Limpia la terminal de manera automatica. 
    '''
    if(name == 'nt'):
        system('cls')
    else:
        system('clear')

def autoDestruccion():
    '''
    Simula la utodestruccion de la consola, a partir de una cuenta 
    regresiva. Incluyendo una "explosion" en codigo ASCII.
    '''
    limpiarTerminal()
    print("\nEsta consola se auto destruira en...")
    sleep(1)
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    limpiarTerminal()

    print("""                                                                                                                                                      
                                                                            .                                                                         
                                                                      ..    .                                                                         
                                                                      ,.  .,.                         .,                                              
                                 ,        .                          (,.  .,,                      %.*,,                                              
                                  ..    . . .                        /,*.,(@..                   .@*#**                                               
                                         ... .%.                    ./.*#*.& ..     /&@@@@@&(,  .@*&(,.                    .                          
                                   / .    ... .(@(.#@(,/*.     .../@@ .@@@@@@@@(@@(........./&@@@@@&(,      .           .*,  ,.                       
                                   .&        .,,... ,,,,((#@@@@@@*#@@@*......(@#.................#@@@@@@&%(#@@@@/     ..#%,*.                         
                                    ((.   .   ..,............#@&&@&&&/.....#@@%.....................,&/.........*@%..../%%,,.                         
                                     %..* ... ,............@@*.........%@@@(.....*//,......../@@@...........*#%#..(%.../@%,*                          
                                   *@&,....... @,........,%...,%@&@@%*..*....(@%//###(@@&@@&%%%%@&....../@&%//@,...%...,%@*,                          
                                   ./,#%&&&&&&@@@/..........@&/(#%%%%%%@(..*@(%%%%%%%%%%@@&&%%%%%&,...*@%%%%#/@*..,(/, ,(#..                          
                                (&@( ........,,,,*,.......%@/#%%%%%%%%%%%@@%%%%%%%&%%%%%%@@%%%%%%%&..(&%%%%%%%@/....*# /*/            .               
                              @@@*..........*#&&#*.......#@(%%%%&@@&%%%%%@@%%%%@@@@@@%%%%&&%%%%%%%%(#&%%%%%%%%@*......#@@@@#,./&@@*,                  
                             @@(.......%@#////%%%%%%@*...@%%%%%@@@@@@%%%%@%%%%&@,...@#%%%&%%%%%%%%%@@%%%%%%%%%@*.......,@@@@@@#,                      
              .            (@&.....*@@///#%%%%%%%%%%%@%..@%%%%%@@,...@%%&@%%%%@#...*@%%%%@%%%@%%%%%%%%%%&%%%%%@%.........@@@@/.                       
                ..... ,/%@@@#....@@&/#%%%%%%%%%%%%%%&@@,.@&%%%%@/....&&%%@%%%%%@..,@%%%%%&%%&@@%%%%%%%%%@%%%%%@&.........,@@@@,.                      
                ...   *%..,&..,@@%%%%%%%&@@@@%%%%%%&@@@@@@@%%%%%@*...@%%%%@%%%%%&@%%%%%%@%%%@@@@%%%%%%%@@&%%%%%@.........#@@ .                        
           .#.../#*,,....., .%@%%%%%%%%%%(..&&%%%%%%%%%%%%%@%%%%%%%&%%%%%%@@%%%%%%%%%%&@@@@@@.@@@%%%%%@@@&%%%%%@&...../ &@.                           
             ./*/***//#@@# .&%%%%%%%%%%%%%%@&%%%%%%%%%%%%%%%&&%%%%%%%%%%%%@@@@%%%%%%@@@........@@%%%@%.%@@%%%%%%%@*...%@@                             
          .....****........,@@@@@@@%%%%%%%%%%%%%%%&@@@%%%%%%%@@@%%%%%%%%@@@...(@@@@@&...........&@@&*..(@@%%%&@@@@/..*@& .                            
                          ,./*..../&@@%%%%%%%%%%@@%..(@%%%%%%@@@*%@@@@@&*...............,..............#@%*.........*@@*.                             
                         %&...........#@@&%%%%%%%%&@@%%%%%%%@@@,.......................,@@@@&*................,.../@@@&((%&&/. ..                     
                       ,@@@@.............#@@&%%%%%%%%%%%%%@@@*........................,@@@@@@@@@@@@%&&@@@@@@@&&&%&&/                                  
                      /*,&@@@(..............(@@%%%%%%%%@@@%..........,@@@@((//**/(#@@@@@@@@%#/*/#&@@,..../@%(%,,.                                     
                      #@@*#@@@@.............%%%%%%&@@@%,.....(@@@@%%@@@@@@@@@@@@@@@@@,........./,...&..... @,,/.                                      
                 ,,,*@@&#(((%@@@@*.........,&&%(*.........&@@@@@@@@@@%/*.. . ,,*/#%@@@@@@%###%(@@&@&,....,.,/,..                                      
             ./*,/@&((*%&,*. (@*,,,(* ................,&@@@@#@@(,**@ .                .******, /@@/.#@(.. ,. ..                                       
          ..  *@/.,%#*,      ***%,     ..  .,%*..,,,.,,((@(,.&,,  ...                              ,   /#.  ..                                        
             .,  ,           ,.#.         ,@/&.../*     %*. #.                                            ,.                                          
                              /.         .%***../       ,  *                                                  .                                       
                                         #, /./.        .                                                                                             
 
    """ )

def login():
    '''
    Solicita al usuario loguearse con un usuario y contraseña, si los datos
    son correctos muestra una secuencia de bienvenida y retorna Verdad, 
    en caso contrario se destruye la terminal.
    '''
    usuario_input = input("Ingrese su usuario: ")
    contraseña_input = input("Ingrese su contraseña: ")

    Acceso = ('Cargando...', 'Aceeso otorgado', 'Bienvenido 007')

    if(usuario == usuario_input and contraseña == contraseña_input):
        for i in Acceso:
            limpiarTerminal()
            print(i)
            sleep(2)

        limpiarTerminal()
        return True
    else:
        print("Error de seguridad...")
        sleep(3)
        autoDestruccion()

def obtenerModo():
    '''Pregunta al usuario que es lo que desea hacer y retorna dicha opcion'''
    while(True):
        modo = input("Desea encriptar o desencriptar un mensaje ?\n")
        modo.lower()
        if(modo in 'encriptar desencriptar'.split()):
            return modo
        else:
            limpiarTerminal()
            print("Error...")
            sleep(3)
            limpiarTerminal()

def obtenerMensaje():
    ''' Solicita al ususario el mensaje a encriptar o desencriptar y lo retorna.'''
    limpiarTerminal()
    return input("Ingrese el mensaje:\n")

def obtenerClave():
    '''
    Solicital al usuario el codigo de cifrado, el cual se comprende entre el 1 y el 26 
    para encriptar o desencriptar un mensaje.
    '''
    limpiarTerminal()
    codigo = 0
    while(True):
        codigo = int(input("Ingrese el codigo de encriptado: "))
        if(codigo >= 1 and codigo <= 26):
            return codigo
        else:
            limpiarTerminal()

def mensajeTraducido(modo, mensaje, codigo):
    '''Encripta o desencripta el mensaje deacuerdo al modo elegido y al cifrado'''
    if(modo == 'desencriptar'):
        codigo = -codigo
    traduccion = '' #Crea una cadena vacia

    for simbolo in mensaje:
        if(simbolo.isalpha()):  #Consulta si los elementos del str son alfebeticos
            num = ord(simbolo)  #Toma el valor ordinal del elemento en ASCII
            num += codigo       #Suma el valor del codigo de encriptado, creando el desplazamiento 
            #Casos especiales
            if(simbolo.isupper()):
                if num > ord('Z'):
                    num -= 26
                elif(num < ord('A')):
                    num += 26
            elif(simbolo.islower()):
                if(num > ord('z')):
                    num -= 26
                elif(num < ord('a')):
                    num += 26
            
            traduccion += chr(num)  #Agrega al str la letra correspondiente al nuevo valor en ASCII
        else:
            traduccion += simbolo   #Agrega al str los simbolos no alfabeticos
    return traduccion

#Bloque principal
if(login() == True):

    modo = obtenerModo()
    mensaje = obtenerMensaje()
    codigo = obtenerClave()

    print("El mensaje traducido es: ")
    print(mensajeTraducido(modo, mensaje, codigo))
    sleep(4)
    autoDestruccion()
