import os
import re

from pprint import pprint

# extracting semesters
ROOT = '../dataset/workbench/'
database = {}
for semester_id in os.listdir(ROOT):
    database[semester_id] = {}
# pprint(database)


# extracting classes
ROOT = '../dataset/workbench/{semester_id}/'
for semester_id in database.keys():
    path = ROOT.replace('{semester_id}', semester_id)
    for class_id in os.listdir(path):
        database[semester_id][class_id] = {}
        # print(f'semester_id={semester_id}, class_id={class_id}')
# pprint(database)


# indentify assessments id
ROOT = '../dataset/workbench/{semester_id}/{class_id}/assessments'
for semester_id in database.keys():
    path = ROOT.replace('{semester_id}', semester_id)
    for class_id in database[semester_id].keys():
        path = path.replace('{class_id}', class_id)
        for assessment_id in os.listdir(path):
            assessment_id = re.sub('.data', '', assessment_id)
            #print(f'semester_id={semester_id}, class_id={class_id}, assessment_id={assessment_id}')
            # print(f'assessment_id={assessment_id}')
            database[semester_id][class_id][assessment_id] = {}
#pprint(database)


# create assessment features
ROOT = '../dataset/workbench/{semester_id}/{class_id}/assessments/'

def add_features(features):
    for semester_id in database.keys():
        for class_id in database[semester_id].keys():
            for assessment_id in database[semester_id][class_id].keys():
                for feature in features:
                    database[semester_id][class_id][assessment_id][feature] = 'NULL'

def extract_features(assessment_file):
    features = []
    for line in assessment_file:
        searched = re.search(r'(\-+\s)([\sa-z]+)(:)', line)
        if searched:
            feature = searched.group(2)
            feature = re.sub(r'\s', '_', feature)
            features.append(feature)
            add_features(features)
            #print(feature)

def open_file(fullpath):
    with open(fullpath, 'r') as assessment_file:
        extract_features(assessment_file)
        

for semester_id in database.keys():
    path = ROOT.replace('{semester_id}', semester_id)
    for class_id in database[semester_id].keys():
        path = path.replace('{class_id}', class_id)
        for assessment_name in os.listdir(path):
            fullpath = os.path.join(path, assessment_name)
            # print(fullpath)
            open_file(fullpath)
            break
        break
    break

pprint(database)