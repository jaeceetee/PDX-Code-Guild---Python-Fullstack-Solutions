# Lab 17 v2 - Quotes API - List quotes by keyword
import requests
import json


while True:

    change_keyword = False
    page = 1
    # Get keyword from user
    keyword = input("Enter a keyword ")
    while change_keyword == False:

        # Build string for URL request
        url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

        # Request content
        response = requests.get(url, headers = headers)
        data = json.loads(response.text)

        # Display content
        for i in range(25):
            print(f'''{(i+1) + (25 * (page - 1))}. "{data["quotes"][i]["body"]}" 
            - by {data["quotes"][i]["author"]}''')

        # More next page or done
        display_option = ">"
        if data['last_page'] == True:
            display_option += "Last Page, enter 'done' to return: "
        else:
            display_option += "Enter 'next' for Next Page or 'done' to return: "
        
        user_response = input(display_option).lower()

        if user_response == 'done':
            change_keyword = True
        elif user_response == 'next':
            page +=1
