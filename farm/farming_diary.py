from farm.corn import Corn


print("\n\n📝 Day One: Corn")

# 1. Instantiate a corn crop
corn = Corn()

# 2. Water the corn crop
corn.water()

# 3. Print "The corn crop produced ## grains"
print(f"The corn crop produced {corn.grains} grains")

# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"
if corn.ripe():
    print("The corn crop is ripe")
else:
    print("The corn crop is not ripe")
