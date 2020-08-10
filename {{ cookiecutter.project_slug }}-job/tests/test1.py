import unittest
from pyspark.sql import SparkSession
from {{ cookiecutter.project_slug }} import *

class PySparkTestCase(unittest.TestCase):

    def setUpClass(self):
        self.spark = SparkSession.builder.appName("testing").getOrCreate()

    def tearDownClass(self):
        self.spark.stop()

class TestApp(PySparkTestCase):
    """
    Every method you want to run a test for must start with `test_`
    """
    def test_function_here(self):
        print("Test Here")
        return True
