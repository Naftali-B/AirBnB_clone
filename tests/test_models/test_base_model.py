#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest module for the BaseModel."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
=======
"""
    contains unittests for the BaseModel class methods.
"""
import json
import unittest
import os
from models.base_model import BaseModel
>>>>>>> naf_tasks

    """Unittests for the BaseModel class."""

<<<<<<< HEAD
    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """To reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instantiation(self):
        """test for instantiation of BaseModel class."""

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_3_init_no_args(self):
        """tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = BaseModel(*args)

    def test_3_attributes(self):
        """tests attribute value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_3_datetime_created(self):
        """Checks if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_3_id(self):
        """Checks for unique user ids."""

        nl = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(nl)), len(nl))

    def test_3_save(self):
        """checks for the public instance method save()."""

        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_str(self):
        """tests for __str__ method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_3_to_dict(self):
        """tests the public instance method to_dict()."""

        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)

    def test_3_to_dict_no_args(self):
        """tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_excess_args(self):
        """tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_4_instantiation(self):
        """Test for instantiation with **kwargs."""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_4_instantiation_dict(self):
        """Test for instantiation with **kwargs from custom dict."""
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_5_save(self):
        """Checks if storage.save() is called from save()."""
        self.resetStorage()
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_5_save_no_args(self):
        """tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
=======
class TestBaseModelMethods(unittest.TestCase):
    """Unittest test class for BaseModel class"""

    def setUp(self):
        """Set up classes to be used to run the tests"""
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def tearDown(self):
        """Tear down the resources that had been setup to run tests"""
        del self.base_1
        del self.base_2

    def test_unique_IDs(self):
        """Test that two instances of BaseModel class are assigned different
            unique IDs
        """
        self.assertNotEqual(self.base_1.id, self.base_2.id)

    def test_kwargs_initialization(self):
        """Test the initialization of a class using kwargs"""
        kwargs = {"__class__": "BaseModel", "created_at":
                  "2021-06-25T19:52:36.252305",
                  "id": "83b3c8a8-b72b-4472-9d80-c52b2e090f04",
                  "updated_at": "2021-06-25T19:52:36.252312"}
        Test_Base = BaseModel(**kwargs)
        self.assertEqual(Test_Base.id, kwargs['id'])
        self.assertEqual(Test_Base.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(Test_Base.updated_at.isoformat(),
                         kwargs['updated_at'])

    def test_str(self):
        """
        Tests method __str__ used in base_model
        """
        base2 = BaseModel()
        self.assertIn("id", base2.__str__())
        self.assertIn("created_at", base2.__str__())
        self.assertIn("updated_at", base2.__str__())
        self.assertIn("[BaseModel]", base2.__str__())
        self.assertTrue(type(base2.__str__()), str)
        self.assertIsNotNone(base2.__str__())

    def test_to_dict(self):
        """Test the return value of the to_dict() method"""
        test_dict = {key: value for key, value in self.base_1.__dict__.items()}
        test_dict['created_at'] = self.base_1.created_at.isoformat()
        test_dict['updated_at'] = self.base_1.updated_at.isoformat()
        test_dict['__class__'] = type(self.base_1).__name__
        self.assertEqual(self.base_1.to_dict(), test_dict)


class Test_Base_Model_save(unittest.TestCase):
    """Unittest class for testing BaseModel's save method"""

    def setUp(self):
        """Set up resources required to run tests"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp")
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def tearDown(self):
        """Tear down resources used to run tests"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tmp"):
            os.rename("tmp", "file.json")
        del self.base_1
        del self.base_2

    def test_updated_at_save(self):
        """Test updated_at attribute is actually updated"""
        time_1 = self.base_1.updated_at
        self.base_1.save()
        self.assertNotEqual(time_1, self.base_1.updated_at)
        self.assertLess(time_1, self.base_1.updated_at)

    def test_object_saved(self):
        """Test whether an object is stored in a file when using save method"""
        self.base_1.save()
        try:
            with open("my_file.json", mode='r', encoding='UTF-8') as f:
                saved_data = json.load(f)

            base_1_id = "BaseModel." + self.base_1.id
            value = saved_data[base_1_id]
            self.assertEqual(value, self.base_1.to_dict())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
>>>>>>> naf_tasks
    unittest.main()
