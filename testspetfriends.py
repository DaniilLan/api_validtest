from api_for_new_test import *
from value import *

a = ApiPets()


class TestPets:
    def test_getkey(self):
        status, res_key = a.get_key(password, email)
        assert status == 200
        assert "key" in res_key

    def test_get_pets(self):
        status, info_pets = a.get_pets(key)
        assert status == 200
        assert "pets" in info_pets
        assert len(info_pets["pets"]) > 0

    def test_create_pet(self):
        status, info = a.create_pet("Цезарь", "Немецкая овчарка", 3, "cezar.jpg")
        assert status == 200
        assert info["id"] == a.get_pets(key)[1]["pets"][0]["id"]

    def test_update_pet(self):
        pet_id = a.get_pets(key)[1]["pets"][0]["id"]  # Для выбора питомца изменять индекс до "id"
        status, info = a.update_pet(pet_id, "Лерой", "Корги", 1)
        assert status == 200
        assert a.get_pets(key)[1]["pets"][0]["name"] == "Лерой"

    def test_delete_pet(self):
        pet_id = a.get_pets(key)[1]["pets"][0]["id"]  # Для выбора питомца изменять индекс до "id"
        len_before = len(a.get_pets(key)[1]["pets"])
        status, info = a.delete_pet(pet_id)
        len_after = len(a.get_pets(key)[1]["pets"])
        assert status == 200
        assert len_before > len_after

    def test_create_pet_simple(self):
        status, info = a.create_pet_simple("Зерглинг", "Зерг", "670")
        assert status == 200
        assert info["pet_photo"] == ''

    def test_set_photo_for_pet(self):
        pet_id = a.get_pets(key)[1]["pets"][0]["id"]  # Для выбора питомца изменять индекс до "id"
        status, info = a.set_photo_for_pet("cezar.jpg", pet_id)
        assert status == 200
        assert a.get_pets(key)[1]["pets"][0]["pet_photo"] != ""

    def test_delete_simple_pet(self):
        pet_id = a.get_pets(key)[1]["pets"][0]["id"]  # Для выбора питомца изменять индекс до "id"
        status, info = a.delete_pet(pet_id)
        assert status == 200
