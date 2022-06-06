def text_replacer(file_path, old_text, new_text):
    """
    Replaces all occurrences of old_text with new_text in input file.
    """
    with open(file_path, 'r') as file:
        file_text = file.read()
    file_text = file_text.replace(old_text, new_text)
    with open(file_path, 'w') as file:
        file.write(file_text)
             

        

