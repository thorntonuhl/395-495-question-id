# coding=utf-8

with open("q_list.txt", "r") as ins:
    content = []
    for line in ins:
        content.append(line)

print content

new_content = []

for line in content:
	line = line.replace("Õ", "'")
	line = line.replace("Ô", "'")
	new_content.append(line)
print new_content


with open("new_q_list.txt", 'wb') as f:
    for line in new_content:
    	f.write(line)

