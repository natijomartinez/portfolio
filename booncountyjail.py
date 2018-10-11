import requests

# Download the HTML

url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
response = requests.get(url)
html = response.content
print html

# Parse the HTML



# Find the table (id=mrc_main_table)



# Get the table rows



# For loop - loop through the <tr>



# Extract the table cells, <td>



# Put all this into a list



# Output the data to a csv file

















