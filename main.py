def file(path):
    *filepath, name = path.split('|')
    return '|'.join(filepath), *name.split('.')


print(file(r'c:|111|222|333|123.txt'))
