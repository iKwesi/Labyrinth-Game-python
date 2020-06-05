from __future__ import absolute_import
import unittest

from Implementation.Labyrinth.labyrinth_manager import LabyrinthManager
from Implementation.Labyrinth.labyrinth_visualizer import Visualizer
from Implementation.Labyrinth.labyrinth import Labyrinth


class TestLabyrinthManager(unittest.TestCase):

    def test_ctor(self):
        """Make sure that the constructor values are getting properly set."""
        manager = LabyrinthManager()

        self.assertEqual(manager.get_labyrinth_count(), 0)
        self.assertEqual(manager.get_all_labyrinth(), [])

    def test_add_new(self):
        """Test adding mazes by passing maze specs into add_maze"""
        manager = LabyrinthManager()

        lab1 = manager.add_labyrinth(6, 6)
        self.assertEqual(lab1.id, 0)
        self.assertEqual(manager.get_all_labyrinth().__len__(), 1)
        self.assertEqual(manager.get_labyrinth_count(), 1)

        lab2 = manager.add_labyrinth(3, 3, 1)
        self.assertEqual(lab2.id, 1)
        self.assertEqual(manager.get_all_labyrinth().__len__(), 2)
        self.assertEqual(manager.get_labyrinth_count(), 2)

    def test_add_existing(self):
        """Test adding mazes by passing already existing Maze objects in"""
        manager = LabyrinthManager()

        lab1 = Labyrinth(2, 2)
        self.assertEqual(lab1.id, 0)
        manager.add_existing_labyrinth(lab1)

        self.assertEqual(manager.get_all_labyrinth().__len__(), 1)
        self.assertEqual(manager.get_labyrinth_count(), 1)
        self.assertIsNotNone(manager.get_labyrinth(lab1.id))
        self.assertEqual(manager.get_labyrinth(lab1.id).id, lab1.id)

        lab2 = Labyrinth(3, 3, 1)
        self.assertEqual(lab2.id, 1)
        manager.add_existing_labyrinth(lab2)

        self.assertEqual(manager.get_all_labyrinth().__len__(), 2)
        self.assertEqual(manager.get_labyrinth_count(), 2)
        self.assertIsNotNone(manager.get_labyrinth(lab2.id))
        self.assertEqual(manager.get_labyrinth(lab2.id).id, lab2.id)

    def test_get_labyrinth(self):
        """Test the get_maze function"""
        manager = LabyrinthManager()

        self.assertEqual(manager.get_labyrinth(0), None)
        self.assertEqual(manager.get_all_labyrinth(), [])
        lab1 = manager.add_labyrinth(6, 6)
        self.assertEqual(lab1.id, 0)

    def test_get_all_labyrinth(self):
        """Tests that get_mazes is returning all mazes"""
        manager = LabyrinthManager()

        self.assertEqual(manager.get_labyrinth(0), None)
        self.assertEqual(manager.get_all_labyrinth(), [])
        manager.add_labyrinth(6, 6)
        manager.add_labyrinth(6, 6)
        all_labs = manager.get_all_labyrinth()
        self.assertAlmostEqual(all_labs.__len__(), 2)

    def test_get_labyrinth_count(self):
        """Tests the get_maze_number function"""
        manager = LabyrinthManager()

        self.assertEqual(manager.get_labyrinth_count(), 0)
        lab1 = Labyrinth(2, 2)
        manager.add_existing_labyrinth(lab1)
        self.assertEqual(manager.get_labyrinth_count(), 1)

    def test_check_matching_id(self):
        """Check that check_matching_id is functioning properly"""

        manager = LabyrinthManager()
        manager.add_labyrinth(8, 8, 1)
        manager.add_labyrinth(8, 8, 1)
        result = [manager.check_matching_id(1)]
        self.assertEqual(len(result), 1)

    # def test_set_filename(self):
    #     """Tests that the filename is getting set"""
    #     manager = LabyrinthManager()
    #     filename = "myFile"
    #     manager.set_filename(filename)
    #     self.assertEqual(filename, manager.media_name)

if __name__ == "__main__":
    unittest.main()
