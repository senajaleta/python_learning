import unittest
import maze
class TestMaze(unittest.TestCase):
    def test_factorial(self):
        #result = maze.factorial(4)
        self.assertEqual(maze.factorial(4),24)
        self.assertEqual(maze.factorial(0), 1)
        self.assertEqual(maze.factorial(1), 1)
    def test_gcd(self):
        result = maze.gcd(12,6)
        self.assertEqual(maze.gcd(12,6),6)
        self.assertEqual(maze.gcd(0,5),5)
        self.assertEqual(maze.gcd(13,15), 15)
        self.assertEqual(maze.gcd(59,59), 59)
if __name__ == '__main__':

    unittest.main()
