def get_unique_element(elements, subject_name):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) >1:
        print("Too many item " + subject_name + " element")
        return None
    else:
        print ("Can't find "+ subject_name+ " name")
        return None
