import sys

with open(sys.argv[1], "r") as file:
	content = file.read()

lines = content.splitlines()

# Strip all lines (remove whitespace)
for i in range(len(lines)):
	lines[i] = lines[i].strip()

# Ensure there is an empty final line
# to ensure a closure of the final paragraph
if lines[-1]:
	lines.append("")

output_line = ""

for i in range(len(lines)):
	if not lines[i]:
		# Set default line type to paragraph
		line_type = "p"

		# Check if heading
		for j in range(len(output_line)):
			if output_line[j] == "#":
				if j == 0:
					line_type = "h1"
				elif output_line[j - 1] == "#":
					if j == 1:
						line_type = "h2"
					elif j == 2:
						line_type = "h3"
					elif j == 3:
						line_type = "h4"
					elif j == 4:
						line_type = "h5"
					elif j == 5:
						line_type = "h6"
		if line_type[0] == "h":
			output_line = output_line[int(line_type[1]):].strip()
		print(f"<{line_type}>{output_line}</{line_type}>")
		output_line = ""
	else:
		if output_line:
			output_line += " "
		output_line += lines[i]
