import unittest

from src.myPet import myPet

maggie = myPet(name="Maggie",
               species="Dog",
               breed="PWD",
               age=0.5,
               is_good=True)

mir = myPet(name = "Mir",
            species="Cat",
            breed="Manx",
            age=13,
            is_good=False
            )

class TestmyPetMethods(unittest.TestCase):

    def test_has_tail(self): 
        self.assertEqual(mir.has_tail(), False)
    
    def test_age_in_months(self): 
        self.assertEqual(mir.age_in_months(), 12*13)
    
    def test_can_swim_true(self): 
        self.assertEqual(maggie.can_swim(), True)
    
    def test_can_swim_false(self):
        self.assertEqual(mir.can_swim(), False)
    
    def test_vocalization(self):
        self.assertEqual(maggie.vocalize(), "BARK")

    def test_cat_vocalizations(self): 
        self.assertEqual(mir.vocalize(),"meow")
    
    def test_pet_energy_level(self): 
        self.assertEqual(maggie.check_energy_level(), "CRAZY")
    
    def test_mir_energy_level(self): 
        self.assertEqual(mir.check_energy_level(), "lazy")

class TestmyPetInit(unittest.TestCase):

    def test_name(self):
        self.assertEqual(maggie.name, "Maggie")
    
    def test_species(self): 
        self.assertEqual(maggie.species, "Dog")
    
    def test_breed(self):
        self.assertEqual(maggie.breed, "PWD")

    def test_age(self): 
        self.assertEqual(maggie.age, 0.5)
    
    def test_is_good(self):
        self.assertEqual(maggie.is_good, True)
    
if __name__ == '__main__':
    unittest.main()