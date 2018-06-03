import json
stt='{"email":"fakeemail@gmail.com","url":"blah.com", "suggestions":[{"name_of_component":"textbox","original_text":"hahahahaah i am fake text please edit me", "altered_text":"hahahahaah I am edited text!!!","lanuage":"Arabic","reason":"poor translation"]}'
su=json.loads(stt)
print(su)
