import json
from bs4 import BeautifulSoup


def get_json_pars():
    with open("index.html") as file:
        src = file.read()

    result = []
    soup = BeautifulSoup(src, "lxml")
    all_courses = soup.find_all("tr")

    for tr in all_courses[1:]:
        courses_data = tr.find_all('td')

        result.append(
            {
                'code': courses_data[3].text.strip(),
                'union': courses_data[4].text.strip(),

            }
        )

    print(result)
    with open("result.json", "w", encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)