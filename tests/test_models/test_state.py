#!/usr/bin/python3
"""test class state Module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()


if __name__ == "__main__":
    unittest.main()
