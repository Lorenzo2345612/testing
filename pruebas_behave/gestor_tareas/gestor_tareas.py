from typing import Literal

class Tarea:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado: Literal["pendiente", "en progreso", "completada"] = "pendiente"

class GestorTareas:
    def __init__(self):
        """Inicializa el gestor de tareas."""
        self.tareas: list[Tarea] = []
        self.contador_id: int = 1


    def agregar_tarea(self, nombre: str, descripcion: str) -> int:
        """Agrega una nueva tarea al gestor.

        Args:
            nombre (str): Nombre de la tarea.
            descripcion (str): Descripción de la tarea.

        Returns:
            int: ID de la tarea agregada.

        Raises:
            ValueError: Si el nombre o la descripción están vacíos.
        """
        if not nombre:
            raise ValueError("El nombre de la tarea no puede estar vacío.")
        if not descripcion:
            raise ValueError("La descripción de la tarea no puede estar vacía.")
        
        tarea = Tarea(self.contador_id, nombre, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea.id
    
    def marcar_completada(self, id: int) -> bool:
        """Marca una tarea como completada.

        Args:
            id (int): ID de la tarea a marcar como completada.

        Returns:
            bool: True si la tarea fue marcada como completada, False si ya estaba completada.

        Raises:
            ValueError: Si no se encuentra una tarea con el ID proporcionado.
        """
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.estado = "completada"
                return True
        raise ValueError(f"No se encontró una tarea con ID {id}.")
    
    def eliminar_tarea(self, id: int) -> bool:
        """Elimina una tarea del gestor.

        Args:
            id (int): ID de la tarea a eliminar.

        Returns:
            bool: True si la tarea fue eliminada.

        Raises:
            ValueError: Si no se encuentra una tarea con el ID proporcionado.
        """
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id:
                self.tareas.pop(i)
                return True
        raise ValueError(f"No se encontró una tarea con ID {id}.")
    
    def obtener_tareas_por_estado(self, estado: str) -> list[Tarea]:
        """Obtiene una lista de tareas filtradas por estado.

        Args:
            estado (Literal["pendiente", "en progreso", "completada"]): Estado por el cual filtrar las tareas.

        Returns:
            list[Tarea]: Lista de tareas que coinciden con el estado proporcionado.
        
        Raises:
            ValueError: Si el estado proporcionado no es válido.
        """
        estados_validos = {"pendiente", "en progreso", "completada"}
        if estado not in estados_validos:
            raise ValueError(f"Estado inválido. Los estados válidos son: {', '.join(estados_validos)}.")
        return [tarea for tarea in self.tareas if tarea.estado == estado]
    