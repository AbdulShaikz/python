post = input("Enter your post : ")

if post.lower().find('abdul') != -1:
    print(f"Post mentions you!")
else:
    print(f"Post didn't mentioned you")