from django.test import TestCase
from django.urls import reverse, resolve
from api.infrastructure.views import DispenseList
from api.infrastructure.models import Dispense

# Create your tests here.
# class apiUrlTest(TestCase):
#     def test_get_dispense_is_resolved(self):
#         url = reverse('api')
#         # print(url)
#         self.assertEquals(resolve(url).func.view_class, DispenseList)
    
class DispenseTestClass(TestCase):
    """
    this test class is one to test the class model Post
    """
    #setupmethod
    def setUp(self):
        self.productname = Dispense(productname= '')

    #testing whether we are being instanciated properly

    def test_instance (self):
        self.assertTrue(isinstance(self.productname, Dispense))


    #testing the save method

    def test_save_method(self):
        self.productname.save_dispense()
        dispenses = Dispense.objects.all()
        self.assertTrue(len(dispenses)>0)
