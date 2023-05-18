import colourswatch.io
import os

for x in os.listdir("./TBC/GIMP GPL/"):
    if x.endswith(".gpl"):
        swotch = colourswatch.io.openSwatch_GPL(f"./TBC/GIMP GPL/{x}")
        colourswatch.io.saveSwatch_JSON(f"./{x}.json", swotch)
        print(f"JSON {x} saved.")
