###########
""" from classifier import classifier
from os import listdir
from os.path import isfile, join

model = "vgg"
images_dir = './pet_images'
#onlyfiles = ['cat_01.jpg', 'Poodle_07927.jpg', 'cat_02.jpg', 'Great_dane_05320.jpg', 'German_shepherd_dog_04890.jpg']
#onlyfiles = ["pet_images/German_shepherd_dog_04890.jpg", "pet_images/Poodle_07927.jpg"]
onlyfiles = [file for file in listdir(images_dir) if isfile(join(images_dir, file))]
my_dictionary = {}
for each_file in onlyfiles:
    #print (each_file)
    file_based_label_list = []
    classification_based_label_list = []
    file_based_label_found = []
    file_name = each_file.split('_')
    lable_list = list(filter(lambda x: ('.jpg' not in x) , file_name))
    lable_list = ' '.join(lable_list).lower()
    file_based_label_list.append(lable_list)
    image_classification = classifier(images_dir + "/" + each_file, model).lower()
    classification_based_label_list.append(image_classification)
    if lable_list in image_classification:
        file_based_label_found.append(1)
    else:
       file_based_label_found.append(0)
    my_dictionary[each_file] = file_based_label_list
    my_dictionary[each_file].extend(classification_based_label_list)
    my_dictionary[each_file].extend(file_based_label_found)
print (my_dictionary) """

""" dogs= []
with open ('dognames.txt') as f:
      dogs = f.read().splitlines()
print (dogs) """

from functools import reduce
my_dict = {'cat_01.jpg': ['cat', 'lynx', 0, 0, 0], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 0, 0], 'cat_02.jpg': ['cat', 'tabby, tabby cat, cat', 1, 0, 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 1, 1], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'gecko_02.jpg': ['gecko', 'banded gecko, gecko', 1, 1, 1]}
cnt = reduce(lambda x, key:x + (my_dict[key][3] & my_dict[key][4]), my_dict, 0)
cnt = reduce(lambda x, key:x + (my_dict[key][3] & 1), my_dict, 0)
cnt = reduce(lambda x, key:x + ((my_dict[key][3] == 0) & (my_dict[key][4] == 0)), my_dict, 0)
cnt = reduce(lambda x, key:x + (my_dict[key][3] == 0), my_dict, 0)
cnt = reduce(lambda x, key:x + ((my_dict[key][2] == 1) & (my_dict[key][3] == 1)), my_dict, 0)
cnt = reduce(lambda x, key:x + (my_dict[key][2] == 1), my_dict, 0)
print (cnt)
