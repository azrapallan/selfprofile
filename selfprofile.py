import sys

args = sys.argv[1:]

if len(args) >= 3:
    hobbies, strength, weakness = args[:3]
else:
    hobbies = "implementing skills"
    strength = "coding skills"
    weakness = "weak in debugging"

print("hobbies:", hobbies)
print("strength:", strength)
print("weakness:", weakness)
print("self_profile:", (hobbies, strength, weakness))

