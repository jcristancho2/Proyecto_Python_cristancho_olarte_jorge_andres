# Importa las librerías necesarias y funciones de módulos
from typing import Dict, List, Optional
import module.utils.validate_data as vd
from module.utils.control_screen import deleteScreen as clean, pauseScreen as pause
from module.create_json.archivosJson import crearJson, leerJson, actualizarJson, mostrarJsonTabla
from tabulate import tabulate

# Añadir elementos ------------------------------------------------

def crearLibrary() -> None:
    """
    Crea y guarda un nuevo libro en 'library.json'.
    """
    clean()
    crearJson('library.json')
    libraryJson = leerJson('library.json')
    
    libros = {
        "id": 0,
        "titulo": '',
        "autor": '',
        "genero": '',
        "valoracion": 0.0
    }
    
    for llave in libros:
        clean()
        if llave == 'valoracion':
            libros[llave] = vd.validatefloat(f'Escriba {llave} del libro: ')
        elif llave == 'id':
            libros[llave] = vd.validateDigit(f'Escriba {llave} del libro: ').lower()
        else:
            libros[llave] = vd.validateAlnum(f'Escriba {llave} del libro: ').lower()
    
    libraryJson.update({libros["titulo"]: libros})
    actualizarJson('library.json', libraryJson)

def crearMusic() -> None:
    """
    Crea y guarda una nueva canción en 'music.json'.
    """
    clean()
    crearJson('music.json')
    musicJson = leerJson('music.json')
    
    musica = {
        "id": 0,
        "titulo": '',
        "autor": '',
        "genero": '',
        "valoracion": 0.0
    }
    
    for llave in musica:
        clean()
        if llave == 'valoracion':
            musica[llave] = vd.validatefloat(f'Escriba {llave} de la canción: ')
        elif llave == 'id':
            musica[llave] = vd.validateDigit(f'Escriba {llave} de la canción: ')
        else:
            musica[llave] = vd.validateAlnum(f'Escriba {llave} de la canción: ').lower()
    
    musicJson.update({musica["titulo"]: musica})
    actualizarJson('music.json', musicJson)

def crearPeli() -> None:
    """
    Crea y guarda una nueva película en 'peli.json'.
    """
    clean()
    crearJson('peli.json')
    peliJson = leerJson('peli.json')
    
    pelicula = {
        "id": 0,
        "titulo": '',
        "autor": '',
        "genero": '',
        "valoracion": 0.0
    }
    
    for llave in pelicula:
        clean()
        if llave == 'valoracion':
            pelicula[llave] = vd.validatefloat(f'Escriba {llave} de la película: ')
        elif llave == 'id':
            pelicula[llave] = vd.validateDigit(f'Escriba {llave} de la película: ')
        else:
            pelicula[llave] = vd.validateAlnum(f'Escriba {llave} de la película: ').lower()
    
    peliJson.update({pelicula["titulo"]: pelicula})
    actualizarJson('peli.json', peliJson)
# view elements ----------------------------------------------
def mostrarLibraryTable():
    """
    Muestra la tabla de la biblioteca.
    """
    data = leerJson("library.json")
    print(tabulate(data.values(), headers="keys", tablefmt="rounded_outline"))
    pause()

def mostrarmusicTable():
    """
    Muestra la tabla de música.
    """
    data = leerJson("music.json")
    print(tabulate(data.values(), headers="keys", tablefmt="rounded_outline"))
    pause()

def mostrarpeliTable():
    """
    Muestra la tabla de películas.
    """
    data = leerJson("peli.json")
    print(tabulate(data.values(), headers="keys", tablefmt="rounded_outline"))
    pause()

# search element ----------------------------------------------
def mostrarelementoTable():
    """
    Busca y muestra un elemento por su nombre.
    """
    clean()
    libraryJson = leerJson('library.json')
    musicJson = leerJson('music.json')
    peliJson = leerJson('peli.json')
    aMostrar = vd.validateAlnum('Escriba el nombre del elemento que desea buscar:\n > ').lower()
    
    if aMostrar in libraryJson:
        data = libraryJson[aMostrar]
        print(tabulate([data], headers="keys", tablefmt="rounded_outline"))
    elif aMostrar in musicJson:
        data = musicJson[aMostrar]
        print(tabulate([data], headers="keys", tablefmt="rounded_outline"))
    elif aMostrar in peliJson:
        data = peliJson[aMostrar]
        print(tabulate([data], headers="keys", tablefmt="rounded_outline"))
    
    pause()

def mostrarelementoautor():
    """
    Busca y muestra elementos por autor.
    """
    clean()
    libraryJson = leerJson('library.json')
    musicJson = leerJson('music.json')
    peliJson = leerJson('peli.json')

    autor_buscado = vd.validateAlnum('Escriba el nombre del autor que desea buscar:\n > ').lower()

    elementos = {**libraryJson, **musicJson, **peliJson}

    resultados = [data for data in elementos.values() if data.get("autor") == autor_buscado]

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No se encontraron elementos de ese autor.")

    pause()

def mostrarelementogenero():
    """
    Busca y muestra elementos por género.
    """
    clean()
    libraryJson = leerJson('library.json')
    musicJson = leerJson('music.json')
    peliJson = leerJson('peli.json')

    genero_buscado = vd.validateAlnum('Escriba el nombre del género que desea buscar:\n > ').lower()

    elementos = {**libraryJson, **musicJson, **peliJson}

    resultados = [data for data in elementos.values() if data.get("genero") == genero_buscado]

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No se encontraron elementos de ese género.")

    pause()

# Editar elementos ----------------------------------------------
def editarNom():
    """
    Edita un elemento por su nombre.
    """
    while True:
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')
        aEditar = vd.validateAlnum('Escriba el nombre del elemento que desea editar: ').lower()
        if aEditar in libraryJson.keys():
            for llave in libraryJson[aEditar]:
                if llave == 'titulo':
                    nNombre = vd.validateAlnum(f'Escriba el {llave} del libro (valor actual {libraryJson[aEditar][llave]})\n > ')
            libraryJson[nNombre] = libraryJson.pop(aEditar)
            print('Actualizado exitosamente')
            actualizarJson('library.json', libraryJson)
            pause()
            break
        elif aEditar in musicJson.keys():
            for llave in musicJson[aEditar]:
                if llave == 'titulo':
                    nNombre = vd.validateAlnum(f'Escriba el {llave} de la canción (valor actual {musicJson[aEditar][llave]})\n > ')
            musicJson[nNombre] = musicJson.pop(aEditar)
            print('Actualizado exitosamente')
            actualizarJson('music.json', musicJson)
            pause()
            break
        elif aEditar in peliJson.keys():
            for llave in peliJson[aEditar]:
                if llave == 'titulo':
                    nNombre = vd.validateAlnum(f'Escriba el {llave} de la película (valor actual {peliJson[aEditar][llave]})\n > ')
            peliJson[nNombre] = peliJson.pop(aEditar)
            print('Actualizado exitosamente')
            actualizarJson('peli.json', peliJson)
            pause()
            break
        else:
            clean()
            print('El elemento no se encuentra en la librería')
            pause()

def editId():
    """
    Edita solo el ID de un elemento por su nombre.
    """
    while True:
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')
        aEditar = vd.validateAlnum('Escriba el nombre del elemento cuyo autor desea editar: ').lower()
        if aEditar in libraryJson.keys():
            libraryJson[aEditar]['autor'] = vd.validateAlnum(f'Escriba el nuevo autor del libro (valor actual {libraryJson[aEditar]["autor"]})\n > ')
            print('Autor actualizado exitosamente')
            actualizarJson('library.json', libraryJson)
            pause()
            break
        
        elif aEditar in musicJson.keys():
            musicJson[aEditar]['autor'] = vd.validateAlnum(f'Escriba el nuevo autor de la canción (valor actual {musicJson[aEditar]["autor"]})\n > ')
            print('Autor actualizado exitosamente')
            actualizarJson('music.json', musicJson)
            pause()
            break
        
        elif aEditar in peliJson.keys():
            peliJson[aEditar]['autor'] = vd.validateAlnum(f'Escriba el nuevo autor de la película (valor actual {peliJson[aEditar]["autor"]})\n > ')
            print('Autor actualizado exitosamente')
            actualizarJson('peli.json', peliJson)
            pause()
            break
        
        else:
            print('El elemento no fue encontrado. Intente de nuevo.')
            pause()

def editarGenero():
    """
    Edita solo el genero de un elemento por su nombre.
    """
    while True:
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')
        aEditar = vd.validateAlnum('Escriba el nombre del elemento cuyo género desea editar: ').lower()
        if aEditar in libraryJson.keys():
            libraryJson[aEditar]['genero'] = vd.validateAlnum(f'Escriba el nuevo género del libro (valor actual {libraryJson[aEditar]["genero"]})\n > ')
            print('Género actualizado exitosamente')
            actualizarJson('library.json', libraryJson)
            pause()
            break
        
        elif aEditar in musicJson.keys():
            musicJson[aEditar]['genero'] = vd.validateAlnum(f'Escriba el nuevo género de la canción (valor actual {musicJson[aEditar]["genero"]})\n > ')
            print('Género actualizado exitosamente')
            actualizarJson('music.json', musicJson)
            pause()
            break
        
        elif aEditar in peliJson.keys():
            peliJson[aEditar]['genero'] = vd.validateAlnum(f'Escriba el nuevo género de la película (valor actual {peliJson[aEditar]["genero"]})\n > ')
            print('Género actualizado exitosamente')
            actualizarJson('peli.json', peliJson)
            pause()
            break
        
        else:
            print('El elemento no fue encontrado. Intente de nuevo.')
            pause()

def editarValoracion():
    while True:
        """
        Edita solo la valoración de un elemento por su nombre.
        """
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')
        
        aEditar = vd.validateAlnum('Escriba el nombre del elemento cuya valoración desea editar: ').lower()
        
        if aEditar in libraryJson.keys():
            libraryJson[aEditar]['valoracion'] = vd.validatefloat(f'Escriba la nueva valoración del libro (valor actual {libraryJson[aEditar]["valoracion"]})\n > ')
            print('Valoración actualizada exitosamente')
            actualizarJson('library.json', libraryJson)
            pause()
            break
        
        elif aEditar in musicJson.keys():
            musicJson[aEditar]['valoracion'] = vd.validatefloat(f'Escriba la nueva valoración de la canción (valor actual {musicJson[aEditar]["valoracion"]})\n > ')
            print('Valoración actualizada exitosamente')
            actualizarJson('music.json', musicJson)
            pause()
            break
        
        elif aEditar in peliJson.keys():
            peliJson[aEditar]['valoracion'] = vd.validatefloat(f'Escriba la nueva valoración de la película (valor actual {peliJson[aEditar]["valoracion"]})\n > ')
            print('Valoración actualizada exitosamente')
            actualizarJson('peli.json', peliJson)
            pause()
            break
        
        else:
            print('El elemento no fue encontrado. Intente de nuevo.')
            pause()

# Eliminar elementos --------------------------------------------
def eliminarElemXnom():
    """
    Elimina un elemento por su nombre.
    """
    while True:
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')
        aEliminar = vd.validateAlnum('Escriba el nombre del elemento que desea eliminar: ').lower()
        
        if aEliminar in libraryJson.keys():
            libraryJson.pop(aEliminar)
            print('Eliminado exitosamente')
            pause()
            actualizarJson('library.json', libraryJson)
            break
        elif aEliminar in musicJson.keys():
            musicJson.pop(aEliminar)
            print('Eliminado exitosamente')
            pause()
            actualizarJson('music.json', musicJson)
            break
        elif aEliminar in peliJson.keys():
            peliJson.pop(aEliminar)
            print('Eliminado exitosamente')
            pause()
            actualizarJson('peli.json', peliJson)
            break
        else:
            clean()
            print('El elemento no se encuentra en la librería')
            pause()

def eliminarXid():
    """
    Elimina un elemento por su ID.
    """
    while True:
        clean()
        libraryJson = leerJson('library.json')
        musicJson = leerJson('music.json')
        peliJson = leerJson('peli.json')

        id = vd.validateAlnum('Ingrese el ID que desea eliminar ->> ')

        json_files = {
            "library.json": libraryJson,
            "music.json": musicJson,
            "peli.json": peliJson
        }

        encontrado = False

        for file_name, data in json_files.items():
            key_to_delete = None
            for key, value in data.items():
                if value.get("id") == id:
                    key_to_delete = key
                    break  # Encontramos el ID, salimos del loop interno
            
            if key_to_delete:
                del data[key_to_delete]  # Eliminamos el elemento
                actualizarJson(file_name, data)  # Guardamos cambios en el archivo correspondiente
                print(f"Elemento con ID {id} eliminado de {file_name}.")
                encontrado = True
        
        if not encontrado:
            print(f"No se encontró un elemento con ID {id}.")

        pause()

# Ver categoría de elementos -------------------------------------

def mostrarcategorialibros():
    """
    Muestra los libros por género/categoría.
    """
    clean()
    libraryJson = leerJson('library.json')
    genero_buscado = vd.validateAlnum('Escriba el nombre del género/categoría que desea buscar:\n > ').lower()

    elementos = {**libraryJson}

    resultados = [data for data in elementos.values() if data.get("genero") == genero_buscado]

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No se encontraron elementos por género.")

    pause()

def mostrarcategoriapeliculas():
    """
    Muestra las películas por género/categoría.
    """
    clean()
    peliJson = leerJson('peli.json')
    genero_buscado = vd.validateAlnum('Escriba el nombre del género/categoría que desea buscar:\n > ').lower()

    elementos = {**peliJson}

    resultados = [data for data in elementos.values() if data.get("genero") == genero_buscado]

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No se encontraron elementos por género.")

    pause()

def mostrarcategoriamusica():
    """
    Muestra la música por género/categoría.
    """
    clean()
    musicJson = leerJson('music.json')
    genero_buscado = vd.validateAlnum('Escriba el nombre del género/categoría que desea buscar:\n > ').lower()

    elementos = {**musicJson}

    resultados = [data for data in elementos.values() if data.get("genero") == genero_buscado]

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No se encontraron elementos por género.")

    pause()

# Guardar y cargar colección -------------------------------------

def savecolecction():
    """
    Guarda la colección de datos en archivos JSON.
    """
    print('Los datos se guardaron correctamente durante la ejecución.')
    pause()

def loadcolecction():
    
    print('Los datos se cargaron correctamente durante la ejecución.')
    pause()

