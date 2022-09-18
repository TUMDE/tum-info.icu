import json
import os

course_json = "./course.json"
elective_modules_urls = [
    "/courses/alg/", "courses/cgv"
]
elective_modules_dirs = ["./" + x for x in elective_modules_urls]

course_page_template = """
# {course_id} {course_name}

Wait for your Contribution 🔥
"""

entry_template = "- [{course_id} {course_name}]({elective_modules_url}{course_id})\n"

with open(course_json, encoding="utf-8") as f:
    courses = json.load(f)

# Basic Data Validation
assert len(courses) == 2  # Will be Adjust After Demo Run
assert all(isinstance(x, dict)for x in courses)

for i in range(len(courses)):
    em, url, dir = courses[i], elective_modules_urls[i], elective_modules_dirs[i]
    sidebar = open(os.path.join(dir, "_sidebar.md"),
                   mode="a", encoding="utf-8")

    readme = open(os.path.join(dir, "README.md"),
                  mode="a", encoding="utf-8")

    # TODO: Decide whether we use sort
    for course_id in sorted(em.keys()):
        course_name = em[course_id]
        course_path = os.path.join(dir, course_id.replace("/", "-")+".md")
        if not os.path.exists(course_path):
            with open(course_path, "w", encoding="utf-8") as page:
                page.write(course_page_template.format(
                    course_id=course_id,
                    course_name=course_name
                ))

        readme.write(entry_template.format(
            course_id=course_id, course_name=course_name, elective_modules_url=url
        ))

        sidebar.write(entry_template.format(
            course_id=course_id,
            course_name=course_name,
            elective_modules_url=url
        ))
