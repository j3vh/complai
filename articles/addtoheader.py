import os

# Set the path to the folder containing the Markdown files
folder_path = "/Users/joas/Documents/GitHub/complai/articles"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a Markdown file
    if filename.endswith(".md"):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename), "r") as f:
            lines = f.readlines()

        # Loop through the lines in the file
        for i, line in enumerate(lines):
            # Check if the line contains the first "---"
            if line.strip() == "---":
                # Add the new line after the first "---"
                lines.insert(i+1, "category: Article\n")
                break

        # Write the modified contents back to the file
        with open(os.path.join(folder_path, filename), "w") as f:
            f.writelines(lines)
