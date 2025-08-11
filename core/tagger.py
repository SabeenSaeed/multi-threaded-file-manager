import re

# Tagging rules using lambdas
EXTENSION_TAGS = {
    'document': lambda f: f['extension'] in ['.txt', '.pdf', '.docx'],
    'image': lambda f: f['extension'] in ['.jpg', '.jpeg', '.png', '.gif'],
    'code': lambda f: f['extension'] in ['.py', '.cpp', '.java', '.js'],
    'video': lambda f: f['extension'] in ['.mp4', '.mov', '.avi'],
    'compressed': lambda f: f['extension'] in ['.zip', '.rar', '.7z'],
}


SIZE_TAGS = {
    'large': lambda f: f['size_kb'] > 1000,
    'tiny': lambda f: f['size_kb'] < 10,
}

NAME_TAGS = {
    'confidential': lambda f: re.search(r'(secret|confidential)', f['name'], re.IGNORECASE),
}

def tag_file(file):
    tags = []

    for tag, rule in EXTENSION_TAGS.items():
        if rule(file):
            tags.append(tag)

    for tag, rule in SIZE_TAGS.items():
        if rule(file):
            tags.append(tag)

    for tag, rule in NAME_TAGS.items():
        if rule(file):
            tags.append(tag)

    return tags

def tag_files(file_list):
    for file in file_list:
        file['tags'] = tag_file(file)
    return file_list
