import requests
import value


class ApiPets:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"
        self.headers = {'accept': 'application/json',
                        "password": value.password,
                        "email": value.email}

    def get_key(self):
        response = requests.get(f"{self.base_url}/api/key", params={'status': 'available'},
                                headers=self.headers)
        status = response.status_code
        try:
            res_key = response.json()
        except:
            res_key = response.text
        return status, res_key

    def get_pets(self):
        response = requests.get(f"{self.base_url}/api/pets",
                                params={'filter': "my_pets"},
                                headers={'auth_key': self.get_key()[1]["key"]})
        status = response.status_code
        try:
            info_pets = response.json()
        except:
            info_pets = response.text
        return status, info_pets

    def create_pet(self):
        file = {'pet_photo': ("cezar.jpg", open("cezar.jpg", 'rb'), 'image/jpg')}
        response = requests.post(f"{self.base_url}/api/pets", headers={'auth_key': self.get_key()[1]["key"]},
                                 data={"name": "Цезарь",
                                       "animal_type": "Немецкая овчарка",
                                       "age": "3"},
                                 files=file)
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def update_pet(self):
        pet_id = self.get_pets()[1]["pets"][0]["id"]  # Изменяем индекс до ["id"], что бы выбрать нужного нам питомца
        response = requests.put(f"{self.base_url}/api/pets/{pet_id}",
                                headers={'auth_key': self.get_key()[1]["key"]},
                                data={"name": "Вики",
                                      "animal_type": "Бульдог",
                                      "age": "2"})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def delete_pet(self):
        pet_id = self.get_pets()[1]["pets"][0]["id"]  # Изменяем индекс до ["id"], что бы выбрать нужного нам питомца
        response = requests.delete(f"{self.base_url}/api/pets/{pet_id}",
                                   headers={'auth_key': self.get_key()[1]["key"]})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def create_pet_simple(self):
        response = requests.post(f"{self.base_url}/api/create_pet_simple",
                                 headers={'auth_key': self.get_key()[1]["key"]},
                                 data={"name": "Вики",
                                       "animal_type": "Бульдог",
                                       "age": "2"})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def set_photo_for_pet(self):
        """Функция добавления фота для питомца"""
        file = {'pet_photo': ("viki.jpg", open("viki.jpg", 'rb'), 'image/jpg')}
        pet_id = self.get_pets()[1]["pets"][0]["id"]  # Изменяем индекс до ["id"], что бы выбрать нужного нам питомца
        response = requests.post(f"{self.base_url}/api/pets/set_photo/{pet_id}",
                                 headers={'auth_key': self.get_key()[1]["key"]},
                                 files=file)
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response


a = ApiPets()
# print(a.get_key())
print(a.get_pets())
# print(a.create_pet())
# print(a.update_pet())
# print(a.delete_pet())
# print(a.create_pet_simple())
# print(a.set_photo_for_pet())
