from avltree import AvlTree
import unittest

class TestAvlTree(unittest.TestCase):
    def setUp(self):
        self.tree = AvlTree[int, str]()
        print('\n[SETUP] Nova arvore AVL inicializada.')

    def test_insert_and_search(self):
        print("[TEST] Inserindo elementos na arvore")
        self.tree[10] = "dez"
        self.tree[20] = "vinte"
        self.tree[5] = "cinco"

        print("[VERIFICACAO] Checking if the element are in tree")
        self.assertEqual(self.tree[10], "dez")
        self.assertEqual(self.tree[20], "vinte")
        self.assertEqual(self.tree[5], "cinco")

        print("[VERIFICACAO] Checking if element is not inserted")
        self.assertNotIn(15, self.tree)

    def test_delete(self):
        print("[TEST] Inserindo elementos PARA REMOCAO")
        self.tree[20] = "vinte"
        self.tree[30] = "trinta"
        self.tree[40] = "quarenta"

        print("[ACAO] Removing 30")
        del self.tree[30]

        print("[VERIFICACAO] Checking if key 30 was removed")
        self.assertNotIn(30, self.tree)

        print("[VERIFICACAO] Checking if other keys remain")
        self.assertIn(20, self.tree)
        self.assertIn(40, self.tree)

    def test_inorder_transversal(self):
        print('[TEST] Inserting elements for inorder transversal')
        elements = [50,30,70,20,40,60,80]
        for i in elements:
            self.tree[i]= str(i)
            print(f"[INSERTION] {i}  -> `{str(i)}`")
            
        print("[ACTION] Performing inorder transversal")
        inorder = list(self.tree)

        print("[RESULT] Ordem obtida: {inorder}")

        self.assertEqual(inorder, sorted(elements))
        print("[SUCESS] Order is correct")

    def test_update_value(self):
        print("[TEST] Testing value update in a key")
        self.tree[100]='cem'
        print(f"[INSERTION] 100 -> 'cem'")
        self.assertEqual(self.tree[100], "cem")



if __name__ == '__main__':
    unittest.main()