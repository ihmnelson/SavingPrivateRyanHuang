
def save_to_file(filename: str, file_contents: str) -> bool:
    try:
        with open(f'files/{filename}.txt', 'w') as file:
            file.write(file_contents)
        return True
    except Exception as e:
        print(f'ERROR: {e}')
        return False


my_file_name = input('What do you want the filename to be: ')
my_file_contents = input('What do you want in the file: ')
print(save_to_file(my_file_name, my_file_contents))

