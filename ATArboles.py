class ArbolNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Crear un árbol de ejemplo
root = ArbolNode(1)
root.left = ArbolNode(2)
root.right = ArbolNode(3)
root.left.left = ArbolNode(4)
root.left.right = ArbolNode(5)
root.right.left = ArbolNode(6)
root.right.right = ArbolNode(7)
#A continuación, implementemos los tres tipos de recorrido:

#Recorrido en preorden: Visita primero el nodo raíz, luego el subárbol izquierdo y finalmente el subárbol derecho.

def pre_order_traversal(node):
    if node is not None:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

print("Recorrido en pre-orden:")
pre_order_traversal(root)
#Recorrido en orden (inorden): Visita primero el subárbol izquierdo, luego el nodo raíz y finalmente el subárbol derecho.

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

print("Recorrido en orden:")
in_order_traversal(root)
#Recorrido en postorden: Visita primero los subárboles izquierdo y derecho y luego el nodo raíz.

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

print("Recorrido en post-orden:")
post_order_traversal(root)
#Estos ejemplos ilustran cómo usar algoritmos de recorrido en árboles para visitar los nodos en diferentes órdenes y realizar operaciones en ellos.
