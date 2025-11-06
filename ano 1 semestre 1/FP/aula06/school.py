# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, 'r') as fin:
        next(fin)
        for line in fin:
            linha = line.strip().split('\t') 
            numero, nome, nota1,nota2 ,nota3 ,  = int(linha[0]), linha[1], float(linha[5]), float(linha[6]), float(linha[7])
            lst.append((numero, nome, nota1, nota2, nota3))
        
        printPauta(notaFinal(lst))
        
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    lst =[]
    for aluno in reg:
        media = ((aluno[2] + aluno[3] + aluno[4])/3)
        aluno = list(aluno)
        aluno.append(media)
        aluno = tuple(aluno)
        lst.append(aluno)
    return lst

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print(f'{"Número":<10} {"Nome":^40} {"Nota":>20}')
    with open(r'C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula06\gravarNotas.txt', 'w') as fout:
        for aluno in lst:
            print(f'{aluno[0]:<10} {aluno[1]:^40} {aluno[-1]:>20.2f}')
            fout.write(f'{aluno[0]:<10} {aluno[1]:^40} {aluno[-1]:>20.2f}\n')



# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile(r"C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula06\school1.csv", lst)
    loadFile(r"C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula06\school2.csv", lst)
    loadFile(r"C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula06\school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


