import unittest
from gestor_tareas import GestorTareas


class TestGestorTareas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Iniciando tests de gestor_tareas")
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinalizando tests de gestor_tareas")

    def setUp(self):
        self.gestor = GestorTareas()

    def tearDown(self):
        self.gestor = None

    def test_agregar_tarea(self):
        """Probando agregar una tarea"""
        id = self.gestor.agregar_tarea("Comprar leche", "Comprar leche en el supermercado")
        self.assertEqual(id, 1)

    def test_agregar_tarea_nombre_vacio(self):
        """Probando agregar una tarea vacía"""
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Nombre vacío")

    def test_agregar_tarea_descripcion_vacia(self):
        """Probando agregar una tarea con descripción vacía"""
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Tarea sin descripción", "")

    def test_marcar_tarea_como_completada(self):
        """Probando marcar una tarea como completada"""
        id = self.gestor.agregar_tarea("Comprar pan", "Comprar pan en la panadería")
        self.assertEqual(len(self.gestor.obtener_tareas_por_estado("completada")), 0)
        resultado = self.gestor.marcar_completada(id)
        self.assertTrue(resultado)
        tareas_completadas = self.gestor.obtener_tareas_por_estado("completada")
        self.assertIn(id, [tarea.id for tarea in tareas_completadas])

    def test_marcar_tarea_ya_completada_como_completada(self):
        """Probando marcar una tarea ya completada como completada"""
        id = self.gestor.agregar_tarea("Comprar pan", "Comprar pan en la panadería")
        resultado = self.gestor.marcar_completada(id)
        self.assertTrue(resultado)
        
    def test_marcar_tarea_no_existente_como_completada(self):
        """Probando marcar una tarea no existente como completada"""
        with self.assertRaises(ValueError):
            self.gestor.marcar_completada(999)

    def test_eliminar_tarea_existente(self):
        """Probando eliminar una tarea existente"""
        id = self.gestor.agregar_tarea("Comprar pan", "Comprar pan en la panadería")
        resultado = self.gestor.eliminar_tarea(id)
        self.assertTrue(resultado)

    def test_eliminar_tarea_no_existente(self):
        """Probando eliminar una tarea no existente"""
        with self.assertRaises(ValueError):
            self.gestor.eliminar_tarea(999)

    def test_obtener_tareas_por_estado(self):
        """Probando obtener tareas por estado"""
        id1 = self.gestor.agregar_tarea("Comprar pan", "Comprar pan en la panadería")
        id2 = self.gestor.agregar_tarea("Comprar leche", "Comprar leche en el supermercado")
        id3 = self.gestor.agregar_tarea("Comprar huevos", "Comprar huevos en la tienda")
        self.gestor.marcar_completada(id1)
        tareas_pendientes = self.gestor.obtener_tareas_por_estado("pendiente")
        tareas_completadas = self.gestor.obtener_tareas_por_estado("completada")
        self.assertIn(id2, [tarea.id for tarea in tareas_pendientes])
        self.assertIn(id1, [tarea.id for tarea in tareas_completadas])

        self.assertEqual(len(tareas_pendientes), 2)
        self.assertEqual(len(tareas_completadas), 1)

    def test_obtener_tareas_por_estado_invalido(self):
        """Probando obtener tareas por estado inválido"""
        with self.assertRaises(ValueError):
            self.gestor.obtener_tareas_por_estado("invalido")

    
