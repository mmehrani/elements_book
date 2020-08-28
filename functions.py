
def is_std_ref(string):
    """
    It finds whether the string has reference in itself.
    """
    return 'Prop.' in string or 'C.N.' in string or 'Post.' in string or 'Def.' in string


def std_ref_form(ref_string):
    """
    Deletes unnecessary chars from the string.
    Seperates combined references.
    returns the refernces in a list.
    """
    if ' corr.' in ref_string:
        ref_string = ref_string.replace(' corr.','')
    
    while ',' in ref_string:
        ref_string = ref_string.replace(', ',']#[')
    
    refs_list = ref_string.split('#')
    return refs_list

def proposition_cleaner(lines):
    """
    Lines is a list of strings dedicated to each propositon proof.
    This function should return its referenced notions in a single list of name strings.
    """
    ref_names = []
    for line in lines:
        for i in range(len(line)):
            if line[i] == '[':
                end_ref = line[i:].find(']') + i
                if is_std_ref(line[i:end_ref + 1]): #check if it has info.
                    ref_names.extend(std_ref_form(line[i: end_ref + 1])) #put the standard refs. in the list.
    
    while '[]' in ref_names:
        ref_names.remove('[]')
    
    return ref_names
