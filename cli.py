from ppio import push

name = input("Enter Name: ")
age = input("Enter Age: ")
year = input("Enter Year: ")
school = input("Enter School: ")
socials = {}
response = ""
print("Enter Socials:")
socials["instagram"] = input("Enter Instagram username: ")
socials["discord"] = input("Enter Discord username: ")
area = []
response = ""
while (response != "done"):
    response: input("Enter Area (type 'done' when done): ")
    area.append(response)
courses = input("Enter Courses")
topics = input("Enter Topics")
bio = input("Enter Bio")
username = input("Enter Username: ")
password = input("Enter Pass: ")
likedby = []

temp_user = {
            "name" : name,
            "age" : age,
            "year" : year,
            "school" : school,
            "socials" : socials,
            "Area" : area,
            "courses": courses,
            "topics": topics,
            "bio": bio,
            "user": username,
            "pass": password,
            "likedby": likedby
}

push.push_to_db(temp_user)
