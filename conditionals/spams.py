spam_comments = ["make a lot of money", "buy now", "subscribe this", "click this"]

comment = input("Enter a comment : ")

processed_comment = comment.lower()

is_spam = False

for keyword in spam_comments:
    if keyword in processed_comment:
        is_spam = True
        break

if is_spam:
    print("WARNING: This comment is detected as SPAM")
else:
    print("This comment is safe.")