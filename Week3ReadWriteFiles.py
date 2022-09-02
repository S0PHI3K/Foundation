# 1. Write the lyrics to a new file called song.txt
# 2. Check that a file has been created successfully.
# 3. The read lines from this file and print out ONLY those lines that have a word
# ‘still’ in them.



import csv

song_lyrics = [
"You could never know what it's like\n"
"Your blood like winter freezes just like ice\n"
"And there's a cold lonely light that shines from you\n"
"You'll wind up like the wreck you hide behind that mask you use\n"
"And did you think this fool could never win?\n"
"Well look at me, I'm coming back again\n"
"I got a taste of love in a simple way\n"
"And if you need to know while I'm still standing, you just fade away\n"
"Don't you know I'm still standing better than I ever did\n"
"Looking like a true survivor, feeling like a little kid\n"
"I'm still standing after all this time\n"
"Picking up the pieces of my life without you on my mind\n"
"I'm still standing (Yeah, yeah, yeah)\n"
"I'm still standing (Yeah, yeah, yeah)\n"
]


#Task1
file = open('song_lyrics.txt', 'a+')
file.writelines(song_lyrics)

#Task3
lines = []
search_word = 'still'
count = 0
with open('song_lyrics.txt', 'r') as file:
for line in file:
line = line.strip()
line = line.lower()
if search_word in line:
lines.append([line])
count += 1
print(lines)
