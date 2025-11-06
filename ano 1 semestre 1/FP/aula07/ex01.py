import unidecode

def readFiles(fname):
    
    abc = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 
        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 
        'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    
    
    with open(fname, 'r', encoding='utf-8') as fin:
        for line in fin:
            print(line)
            line = unidecode(line.lower())
            
            for char in line:
                print(char)
                if char.isalpha():
                    print(char)
                    abc[char] += 1

    for letter in sorted(abc.keys()):
        print(f"{letter}: {abc[letter]}")
   


file1 = r'C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula07-20241105T112609Z-001\aula07\examples\pg3333.txt'
if __name__ == "__main__":
        readFiles(file1)