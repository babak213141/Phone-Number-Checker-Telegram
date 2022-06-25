# Phone-Number-Checker-Telegram

```
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
```
