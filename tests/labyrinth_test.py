from __future__ import absolute_import
import unittest

from Implementation.Labyrinth.labyrinth import Labyrinth
from Implementation.Labyrinth.cell import Cell


def generate_labyrinth():
    # Used to generate a 5x5 maze for testing, Feel free to modify as needed

    cols = 5
    rows = 5
    return Labyrinth(rows, cols)


class TestLabyrinth(unittest.TestCase):
    def test_ctor(self):
        """Make sure that the constructor values are getting properly set."""
        cols = 5
        rows = 5
        lab = Labyrinth(rows, cols)

        self.assertEqual(lab.num_cols, cols)
        self.assertEqual(lab.num_rows, rows)
        self.assertEqual(lab.id, 0)
        self.assertEqual(lab.grid_size, rows*cols)

        id=33
        lab2 = Labyrinth(rows, cols, id)
        self.assertEqual(lab2.num_cols, cols)
        self.assertEqual(lab2.num_rows, rows)
        self.assertEqual(lab2.id, id)
        self.assertEqual(lab2.grid_size, rows * cols)

    def test_generate_grid(self):
        lab = generate_labyrinth()
        grid = lab.generate_grid()

        self.assertEqual(len(grid), lab.num_cols)
        self.assertGreater(len(grid), 2)
        self.assertEqual(len(grid[0]), lab.num_rows)

    def test_find_neighbors(self):
        lab = Labyrinth(2, 2)
        neighbors = lab.find_neighbours(0, 1)
        self.assertIsNotNone(neighbors)


if __name__ == "__main__":
    unittest.main()