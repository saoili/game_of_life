from unittest import TestCase, main
from game_of_life import GameOfLife


class TestGameOfLifeGrid(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_total_around(self):
        """
        Currently doesn't give meaningful fails
        TO DO - meaningful fails!
        """
        g = GameOfLife(6, 4)
        """
        ---x--
        --x---
        -x----
        x-x-x-
        """
        g.grid[(3, 0)] = 1
        g.grid[(2, 1)] = 1
        g.grid[(1, 2)] = 1
        g.grid[(0, 3)] = 1
        g.grid[(2, 3)] = 1
        g.grid[(4, 3)] = 1

        expected = {
            (0, 0): 1,
            (1, 0): 3,
            (2, 0): 3,
            (3, 0): 4,
            (4, 0): 2,
            (5, 0): 2,
            (0, 1): 1,
            (1, 1): 2,
            (2, 1): 3,
            (3, 1): 2,
            (4, 1): 1,
            (5, 1): 0,
            (0, 2): 2,
            (1, 2): 4,
            (2, 2): 3,
            (3, 2): 3,
            (4, 2): 1,
            (5, 2): 2,
            (0, 3): 2,
            (1, 3): 3,
            (2, 3): 3,
            (3, 3): 3,
            (4, 3): 2,
            (5, 3): 2
        }

        for key in g.grid:
            self.assertEqual(g.total_around(*key), expected[key])

    def test_next_value(self):
        # tests where the current field is alive
        g = GameOfLife(3)
        g.grid[(1, 1)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # underpopulation
        g.grid[(0, 0)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # underpopulation
        g.grid[(0, 1)] = 1
        self.assertEqual(g.next_value(1, 1), 1)  # survives
        g.grid[(0, 2)] = 1
        self.assertEqual(g.next_value(1, 1), 1)  # survives
        g.grid[(1, 0)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # overpopulation

        # tests where the current field is not alive
        g = GameOfLife(3)
        self.assertEqual(g.next_value(1, 1), 0)  # no new life
        g.grid[(1, 1)] = 0
        self.assertEqual(g.next_value(1, 1), 0)  # no new life
        g.grid[(0, 0)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # no new life
        g.grid[(0, 1)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # no new life
        g.grid[(0, 2)] = 1
        self.assertEqual(g.next_value(1, 1), 1)  # new life!
        g.grid[(1, 0)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # no new life
        g.grid[(1, 2)] = 1
        self.assertEqual(g.next_value(1, 1), 0)  # no new life


if __name__ == "__main__":
    main()
