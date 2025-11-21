import sys
if len(sys.argv) > 3:
    hobbies = sys.argv[1]
    strength = sys.argv[2]
    weakness = sys.argv[3]
else:
    hobbies = "implementing skills"
    strength = "coding skills"
    weakness = "weak in debugging"
self_profile = (hobbies, strength, weakness)
print("hobbies:", hobbies)
print("strength:", strength)
print("weakness:", weakness)
print("self_profile:", self_profile)
