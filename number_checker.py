from pyrogram import Client
from pyrogram.types import InputPhoneContact
class NumberChecker:
    def __init__(self, api_id=None, api_hash=None, phone_number=None, session_name=None, app: Client=None):
        if all(session_name, api_id, api_hash, phone_number):
            self.app = Client(session_name, api_id, api_hash, phone_number=phone_number)
        elif app:
            self.app.start()
    def getPhones(self, listOfPhones: list[str]):
        if listOfPhones:
            check = self.app.import_contacts([InputPhoneContact(phone, "") for phone in listOfPhones])
            importedUsers = [user.user_id for user in check.imported]
            importedPhones = [phone.phone for phone in check.users]
            self.app.delete_contacts(importedUsers)
            filterIN = lambda x: list(
                                        (
                                        filter(
                                            lambda y: y not in x, listOfPhones
                                        )
                                    )
                                )
            return {
                "success": True,
                "result":{
                    "Good":
                        filterIN(importedPhones),
                    "Bad":
                        importedPhones
                    },
                "Note": "شماره تلفن های خوب ممکن است بن شده باشند"
                }
        else:
            return {
                "success": False
            }

if __name__ == '__main__':
    api_id = 123456
    api_hash = "80b54f07..."
    checker = NumberChecker(
        api_id, # API_ID
        api_hash, # Api_Hash
        "98911390...", # PhoneNumber
        "main" # SessionName
    ) 
    # Or Use:
    # app = Client() 
    #   checker = NumberChecker(app=app) -> (app: pyrogram.Client) 
    from json import dumps
    result = (
        checker.getPhones(
            [
                "+13154968490",
                "+13153162838",
                "+13155383092",
                "+13157263261",
                "+13152104671"
            ]
        )   
    )
    print(
        dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )
    # Results:
    #   {
    #       "success": true,
    #       "result": {
    #           "Good": [
    #               "+13154968490",
    #               "+13153162838",
    #               "+13155383092",
    #               "+13157263261",
    #               "+13152104671"
    #           ],
    #           "Bad": [
    #               "13157263261"
    #           ]
    #       },
    #       "Note": "شماره تلفن های خوب ممکن است بن شده باشند"
    #   }
