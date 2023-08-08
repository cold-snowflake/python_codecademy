
# guests = {}


# def read_guestlist(file_name):
#   text_file = open(file_name,'r')
#   while True:
#     line_data = text_file.readline().strip().split(",")
#     if len(line_data) < 2:
#     # If no more lines, close file
#       text_file.close()
#       break
#     name = line_data[0]
#     age = int(line_data[1])
#     guests[name] = age
#     yield name

# guest_list = 'guest_list.txt'
# guest_list_iter =  read_guestlist(guest_list)
# for item in range(10):
#   print(next(guest_list_iter))

# next(guest_list_iter)
# guest_list_iter.send("Jane,35")

# # print(guest_list_iter)
# # for item in range(5):
# #   print(next(guest_list_iter))

# value = guest_list_iter. __iter__
# for item in value:
#   print(item)

# guests = {}
# def read_guestlist(file_name):
#     text_file = open(file_name,'r')
#     while True:
#         x = yield
#         if x is None:
#           line_data = text_file.readline().strip().split(",")
#         else:
#           line_data = x.split(",")
#         if len(line_data) < 2:
#         # If no more lines, close file
#             text_file.close()
#             break
#         name = line_data[0]
#         age = int(line_data[1])
#         guests[name] = age
#         yield name 
                                            
# guestlist = read_guestlist('guest_list.txt')

# for k in range(20):
#   print(next(guestlist))

# #Add Jane,35 to the generator
# next(guestlist)
# guestlist.send("Jane,35")

# for k in range(8):
#   print(next(guestlist))

# def guest_age(guest_dict):
#   for key,val in guest_dict.items():
#     if val > 21:
#       yield key

# age_of_guest = guest_age(guests)

# for obj in age_of_guest:
#   print(obj)


# def table_one():
#   for j in range(1,2):
#     for k in range(1,6):
#       yield "Chicken", "Table {}".format(j),"Seat {}".format(k)

# def table_two():
#   for j in range(2,3):
#     for k in range(6,11):
#       yield "Beef", "Table {}".format(j), "Seat {}".format(k)

# def table_three():
#   for j in range(3,4):
#     for k in range(11,16):
#       yield "Fish", "Table {}".format(j), "Seat {}".format(k)


# def combined_tables():
#   yield from table_one()
#   yield from table_two()
#   yield from table_three()

# combined_tables = combined_tables()

# def guest_assignment():
#   for name in guests.keys():
#     yield name, next(combined_tables)

# guest_assignment = guest_assignment()
# for person in guest_assignment:
#   print(person)



guests = {}
def read_guestlist(file_name):
    text_file = open(file_name,'r')
    while True:
        x = yield
        if x is None:
          line_data = text_file.readline().strip().split(",")
        else:
          line_data = x.split(",")
        if len(line_data) < 2:
        # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        yield name 
                                            
guestlist = read_guestlist('guest_list.txt')

for k in range(20):
  print(next(guestlist))

#Add Jane,35 to the generator
next(guestlist)
guestlist.send("Jane,35")

for k in range(8):
  print(next(guestlist))

def guest_age(guest_dict):
  for key,val in guest_dict.items():
    if val > 21:
      yield key

age_of_guest = guest_age(guests)

for obj in age_of_guest:
  print(obj)

def table_one():
  for j in range(1,2):
    for k in range(1,6):
      yield "Chicken", "Table {}".format(j),"Seat {}".format(k)

def table_two():
  for j in range(2,3):
    for k in range(6,11):
      yield "Beef", "Table {}".format(j), "Seat {}".format(k)

def table_three():
  for j in range(3,4):
    for k in range(11,16):
      yield "Fish", "Table {}".format(j), "Seat {}".format(k)


def combined_tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

combined_tables = combined_tables()

def guest_assignment():
  for name in guests.keys():
    yield name, next(combined_tables)

guest_assignment = guest_assignment()
for person in guest_assignment:
  print(person)



