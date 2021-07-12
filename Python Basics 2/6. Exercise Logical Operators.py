is_magician = False
is_expert = True

# Check if magician and expert: "You are a master magician"
# Check if magician but not expert: "At least you are getting there"
# Check if you are not magician: "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician!!")
elif is_magician and not is_expert:
    print("At least you are getting there!!")
elif not is_magician:
    print("You need magic powers!!")