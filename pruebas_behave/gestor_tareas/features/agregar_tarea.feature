# language: es

Característica: Agregar tareas al gestor
    Como usuario del gestor de tareas
    Quiero poder agregar nuevas tareas
    Para mantener un registro de las tareas pendientes

    Escenario: Agregar una tarea exitosamente
        Dado que el gestor de tareas está vacío
        Cuando agrego una tarea con nombre "Comprar leche" y descripción "Comprar leche en el supermercado"
        Entonces la tarea se agrega exitosamente con ID 1
        Y el gestor tiene 1 tarea
        Y la tarea con ID 1 tiene nombre "Comprar leche"
        Y la tarea con ID 1 tiene descripción "Comprar leche en el supermercado"
        Y la tarea con ID 1 tiene estado "pendiente"

    Escenario: Agregar múltiples tareas
        Dado que el gestor de tareas está vacío
        Cuando agrego una tarea con nombre "Comprar pan" y descripción "Comprar pan en la panadería"
        Y agrego una tarea con nombre "Comprar huevos" y descripción "Comprar huevos en la tienda"
        Y agrego una tarea con nombre "Hacer ejercicio" y descripción "Ir al gimnasio por 1 hora"
        Entonces el gestor tiene 3 tareas
        Y la tarea con ID 1 tiene nombre "Comprar pan"
        Y la tarea con ID 2 tiene nombre "Comprar huevos"
        Y la tarea con ID 3 tiene nombre "Hacer ejercicio"

    Escenario: Intentar agregar tarea con nombre vacío
        Dado que el gestor de tareas está vacío
        Cuando intento agregar una tarea con nombre vacío y descripción "Nombre vacío"
        Entonces se produce un error con mensaje "El nombre de la tarea no puede estar vacío"
        Y el gestor tiene 0 tareas

    Escenario: Intentar agregar tarea con descripción vacía
        Dado que el gestor de tareas está vacío
        Cuando intento agregar una tarea con nombre "Tarea sin descripción" y descripción vacía
        Entonces se produce un error con mensaje "La descripción de la tarea no puede estar vacía"
        Y el gestor tiene 0 tareas

    Escenario: El contador de ID se incrementa correctamente
        Dado que el gestor de tareas está vacío
        Cuando agrego una tarea con nombre "Primera tarea" y descripción "Descripción de la primera"
        Y agrego una tarea con nombre "Segunda tarea" y descripción "Descripción de la segunda"
        Entonces la tarea con ID 1 tiene nombre "Primera tarea"
        Y la tarea con ID 2 tiene nombre "Segunda tarea"

    Escenario: Las tareas nuevas se crean con estado pendiente
        Dado que el gestor de tareas está vacío
        Cuando agrego una tarea con nombre "Tarea nueva" y descripción "Una tarea recién creada"
        Entonces la tarea con ID 1 tiene estado "pendiente"