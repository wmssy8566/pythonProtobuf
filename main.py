import person_pb2

first_info = person_pb2.AddressBook()
person = first_info.people.add()


person.name = "Shany"
person.id = 99
person.email = "aaa@sohu.com"

phone = person.phones.add()
phone.number = "82081234"
phone.type = person.PhoneType.MOBILE

#序列化
serializeToString = first_info.SerializeToString()
print(serializeToString, type(serializeToString))


first_info.ParseFromString(serializeToString)

for person in first_info.people:
  print("name: {}, id: {}, email: {}".format(person.name, person.id, person.email))

  for phone_number in person.phones:
    print(phone_number.number, phone_number.type)


