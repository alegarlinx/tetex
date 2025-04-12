# Tetris Game

Este es un proyecto de juego de Tetris implementado en Python para ser jugado en la terminal de Kali Linux.

## Requisitos

Asegúrate de tener Python 3 instalado en tu sistema. Este proyecto utiliza la biblioteca `curses` para la interfaz de terminal. Puedes instalar las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
tetris-game
├── src
│   ├── main.py          # Punto de entrada del juego
│   ├── game
│   │   ├── board.py     # Clase que representa el tablero de Tetris
│   │   ├── tetromino.py  # Clase que representa las piezas del juego
│   │   └── utils.py      # Funciones auxiliares para el juego
│   └── assets
│       └── __init__.py   # Inicializa el paquete de assets
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## Cómo Ejecutar el Juego

Para ejecutar el juego, navega al directorio `src` y ejecuta el siguiente comando:

```
python main.py
```

Disfruta del juego y trata de obtener la puntuación más alta posible. ¡Buena suerte!