import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

class TestShoppingCart(unittest.TestCase):
    def setUp(self): # metodo que se ejecuta antes de la pruebas
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self): # metodo que se ejecuta desues de la pruebas
        pass

    def test_cinco_mas_cinco_igual_dies(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_pan(self): # comprobar si el nombre del  producto se igual a otro
        self.assertEqual(self.pan.name, "Pan")

    def test_nombre_producto_diferente_manzana(self): # comprobar si el nombre del  producto No es igual a otro
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self): # comprobar si un carrito contiene un producto
        self.assertTrue(self.shopping_cart.constains_items())

    def test_no_contiene_productos(self): # comprobar si un carrito No contiene un producto
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.constains_items())

    def test_obtener_productos_pan(self): # comprobar si dos objetos son los mismos
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo) # comprobar si dos objetos No son los mismos

    def test_exeption_al_obtener_jugo(self): # lanzar error si no consigue el producto
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_com_un_productos(self): # comprobar el total del carrito
        total = self.shopping_cart.total()
        self.assertGreater(total, 0) # mayor a 0
        self.assertLess(total, self.pan.price + 1.0) # menor a 1.0
        self.assertEqual(total, self.pan.price) # igual

    def test_codigo_pan(self): # validar que el nombre del prodcuto se encuentar dentro del codigo
        self.assertRegex(self.pan.code(), self.pan.name )

    def test_fail(self): # no esta dentro de la libreria y sirve para hacer test manual
        if 2 > 3:
            self.fail("Dos no es mayor a test!")

    API_VERSION = 17
    # @unittest.skip("Colocamos nuestros motivos") # el programador quiere saltarse la prueba y sabe el porque
    # @unittest.skipIf(API_VERSION < 18,"la version es obsoleta") # el programador quiere saltarse la prueba y debe cumplirse una condicion
    @unittest.skipUnless(3 > 5,"Colocamos nuestros motivos")
    def test_prueba_skip(self):
        pass

if __name__ == '__main__':
    unittest.main()