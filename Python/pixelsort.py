from PIL import Image
def sort_row(row): # Pixel sorting: load all pixels, loop through each row, sort row
	min, min_index = 255*3, 0
	for i in range(len(row)): # find the darkest pixel in the row
		temp = row[i][0] + row[i][1] + row[i][2]
		if temp < min: min = temp
		min_index = i# sort the row up the brightest pixel
	sorted_row = row[:min_index]
	sorted_row.sort()
	return sorted_row + row[min_index:]

img = Image.open(“motorboat.jpg”) # load the pixel data from the file.
pixels = img.load()
width, height = img.size
for y in range(height):  # loop through each row and sort the pixels in that row
	row = []  # get a row
	for x in range(width): row.append(pixels[x,y]) # sort the row
	row = sort_row(row) # record the sorted data
	for x in range(width): pixels[x,y] = row[x] # to make new image, data > list
sorted_pixels = []
for y,x in range(height),range(width):
	sorted_pixels.append(pixels[x,y])
new_img = Image.new(‘RGB’,(width, height))
new_img.putdata(sorted_pixels)
new_img.show() # preview the sorted image.
new_img.save(“motorboat_sorted.jpg”) # save the file with a new name.