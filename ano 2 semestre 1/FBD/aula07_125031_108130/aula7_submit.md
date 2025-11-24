# BD: Guião 7


## ​7.2 
 
### *a)*

```
A relação está na primeira forma normal (1FN), já que os atributos são atómicos.

Para ser considerada segunda forma normal (2FN), teriamos que:
-> Livro(Titulo_Livro [PK], Nome_Autor [FK], Tipo_Livro, Preco, NoPaginas, Editor, Endereco_Editor, Ano_Publicacao)
-> Autor(Nome_autor [PK], Afiliacao_Autor)
```

### *b)* 

```
Para transformar numa relação de terceira forma normal (3FN):
- primeiro temos que passar para uma segunda forma normal (2FN), decompondo o Livro para Autor(Nome_autor [PK], Afiliacao_Autor)
- de 2FN para 3FN, temos que remover as dependências transitivas, ou seja, criando a entidade TipoLivro(TipoLivro [PK], NumPaginas [PK], Preco) e Editor(NomeEditor [PK], EndereçoEditor)

Ficando assim com:
Livro(Titulo_Livro [PK], Nome_Autor [FK], Editor [FK], Tipo_Livro [FK], NoPaginas [FK], Ano_Publicacao)
Autor(Nome_autor [PK], Afiliacao_Autor)
TipoLivro(TipoLivro [PK], NumPaginas [PK], Preco)
Editor(NomeEditor [PK], EndereçoEditor)
```


## ​7.3
 
### *a)*

```
... Write here your answer ...
```


### *b)* 

```
... Write here your answer ...
```


### *c)* 

```
... Write here your answer ...
```


## ​7.4
 
### *a)*

```
A chave é {A, B}
```


### *b)* 

```
R1(A, B, C, D); F = {{A,B} -> {C,D}, {C} -> {A}}
R2 = {D, E}; F = {{D} -> {E}}
```


### *c)* 

```
(continuando do R2 da alínea b)

R3 = {C, A}; F = {{C} -> {A}}
R4 = {B, C, D}; F = {{B,C} -> {D}}
```



## ​7.5
 
### *a)*

```
A chave é  {A,B}
```

### *b)* 

```
R1 (A, C, D); F1 = { A → C, C → D }
R2 (A, B, E); F2 = { A,B → E }
```


### *c)* 

```
R1a (A, C); F = { A → C }
R1b (C, D); F = { C → D }
R2  (A, B, E); F = { A,B → E }
```

### *d)* 

```
A decomposição para 3FN já se encontra em BCNF.
```
