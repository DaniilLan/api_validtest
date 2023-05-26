from api import *

a = ApiPets()


class TestPets:
    def test_getkey(self):
        status, res_key = a.get_key()
        assert status == 200
        assert "key" in res_key

    def test_get_pets(self):
        status, info_pets = a.get_pets()
        assert status == 200
        assert "pets" in info_pets
        assert len(info_pets["pets"]) > 0

    def test_create_pet(self):
        status, info = a.create_pet()
        assert status == 200
        assert info["id"] == a.get_pets()[1]["pets"][0]["id"]

    def test_update_pet(self):
        status, info = a.update_pet()
        assert status == 200

    def test_delete_pet(self):
        status, info = a.delete_pet()
        assert status == 200

    def test_create_pet_simple(self):
        status, info = a.create_pet_simple()
        assert status == 200
        assert info["pet_photo"] == ''

    def test_set_photo_for_pet(self):
        status, info = a.set_photo_for_pet()
        assert status == 200

    def test_delete_simple_pet(self):
        status, info = a.delete_pet()
        assert status == 200
