import fnmatch
import os
import shutil


def create_folders(default_path):
    models_path = default_path + 'models/'
    sample_path = default_path + 'sample/'
    validation_path = default_path + 'valid/'
    sample_train = sample_path + 'train/'
    sample_train_dogs = sample_train + 'dogs'
    sample_train_cats = sample_train + 'cats'
    sample_validation = sample_path + 'valid/'
    sample_validation_dogs = sample_validation + 'dogs'
    sample_validation_cats = sample_validation + 'cats'
    train_dogs = default_path + 'train/dogs/'
    train_cats = default_path + 'train/cats/'
    validation_dogs = validation_path + 'dogs/'
    validation_cats = validation_path + 'cats/'

    if not os.path.exists(models_path):
        os.mkdir(path=models_path)

    if not os.path.exists(sample_path):
        os.mkdir(sample_path)

    if not os.path.exists(validation_path):
        os.mkdir(validation_path)

    if not os.path.exists(sample_train):
        os.mkdir(sample_train)

    if not os.path.exists(sample_train_dogs):
        os.mkdir(sample_train_dogs)

    if not os.path.exists(sample_train_cats):
        os.mkdir(sample_train_cats)

    if not os.path.exists(sample_validation):
        os.mkdir(sample_validation)

    if not os.path.exists(sample_validation_dogs):
        os.mkdir(sample_validation_dogs)

    if not os.path.exists(sample_validation_cats):
        os.mkdir(sample_validation_cats)

    if not os.path.exists(train_dogs):
        os.mkdir(train_dogs)

    if not os.path.exists(train_cats):
        os.mkdir(train_cats)

    if not os.path.exists(validation_dogs):
        os.mkdir(validation_dogs)

    if not os.path.exists(validation_cats):
        os.mkdir(validation_cats)


def prepare_training_file(default_path):
    src_files = os.listdir(default_path + 'train')
    dogs_train = default_path + 'train/dogs'
    cats_train = default_path + 'train/cats'
    for file in src_files:
        full_file_name = os.path.join(default_path + 'train', file)
        if fnmatch.fnmatch(file, 'dog.*'):
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dogs_train)
                os.remove(default_path + 'train/' + str(file))
        if fnmatch.fnmatch(file, 'cat.*'):
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, cats_train)
                os.remove(default_path + 'train/' + str(file))


def prepare_validation_file(default_path):
    src_files_cat = os.listdir(default_path + 'train/cats')
    src_files_dog = os.listdir(default_path + 'train/dogs')
    valid_dog = default_path + 'valid/dogs'
    valid_cat = default_path + 'valid/cats'
    for counter in range(0, 1000):
        full_file_name_cat = os.path.join(default_path + 'train/cats', src_files_cat[counter])
        full_file_name_dog = os.path.join(default_path + 'train/dogs', src_files_dog[counter])
        if os.path.isfile(full_file_name_cat):
            shutil.copy(full_file_name_cat, valid_cat)
            os.remove(default_path + 'train/cats/' + str(src_files_cat[counter]))
        if os.path.isfile(full_file_name_dog):
            shutil.copy(full_file_name_dog, valid_dog)
            os.remove(default_path + 'train/dogs/' + str(src_files_dog[counter]))


def prepare_sample_file(default_path):
    src_files_cat = os.listdir(default_path + 'train/cats')
    src_files_dog = os.listdir(default_path + 'train/dogs')
    sample_train_dog = default_path + 'sample/train/dogs'
    sample_train_cat = default_path + 'sample/train/cats'
    sample_valid_dog = default_path + 'sample/valid/dogs'
    sample_valid_cat = default_path + 'sample/valid/cats'
    for counter in range(0, 12):
        full_file_name_cat = os.path.join(default_path + 'train/cats', src_files_cat[counter])
        full_file_name_dog = os.path.join(default_path + 'train/dogs', src_files_dog[counter])
        if os.path.isfile(full_file_name_cat):
            shutil.copy(full_file_name_cat, sample_train_cat)
        if os.path.isfile(full_file_name_dog):
            shutil.copy(full_file_name_dog, sample_train_dog)

    dog_for_valid = os.listdir(default_path + 'sample/train/dogs')
    cat_for_valid = os.listdir(default_path + 'sample/train/cats')
    for counter in range(0, 4):
        full_file_name_cat = os.path.join(default_path + 'sample/train/cats', cat_for_valid[counter])
        full_file_name_dog = os.path.join(default_path + 'sample/train/dogs', dog_for_valid[counter])
        if os.path.isfile(full_file_name_cat):
            shutil.copy(full_file_name_cat, sample_valid_cat)
            os.remove(default_path + 'sample/train/cats/' + str(src_files_cat[counter]))
        if os.path.isfile(full_file_name_dog):
            shutil.copy(full_file_name_dog, sample_valid_dog)
            os.remove(default_path + 'sample/train/dogs/' + str(src_files_dog[counter]))


def main():
    default_path = '/home/vishesh/kaggle/'
    # create_folders(default_path)
    # prepare_training_file(default_path)
    # prepare_validation_file(default_path)
    prepare_sample_file(default_path)


if __name__ == "__main__":
    main()
