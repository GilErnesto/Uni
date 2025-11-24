# BD: Guião 6

## Problema 6.1

### *a)* Todos os tuplos da tabela autores (authors);

```
SELECT * FROM authors
```

### *b)* O primeiro nome, o último nome e o telefone dos autores;

```
SELECT au_lname, au_fname, phone FROM authors
```

### *c)* Consulta definida em b) mas ordenada pelo primeiro nome (ascendente) e depois o último nome (ascendente); 

```
SELECT au_lname, au_fname, phone 
FROM authors
ORDER BY au_lname ASC, au_fname ASC;
```

### *d)* Consulta definida em c) mas renomeando os atributos para (first_name, last_name, telephone); 

```
SELECT au_lname AS first_name, au_fname AS last_name, phone AS telephone
FROM authors 
ORDER BY first_name ASC, last_name ASC;
```

### *e)* Consulta definida em d) mas só os autores da Califórnia (CA) cujo último nome é diferente de ‘Ringer’; 

```
SELECT au_lname AS first_name, au_fname AS last_name, phone AS telephone FROM authors
WHERE au_fname != 'Ringer' AND state ='CA'
ORDER BY first_name ASC, last_name ASC;
```

### *f)* Todas as editoras (publishers) que tenham ‘Bo’ em qualquer parte do nome; 

```
SELECT pub_name, pub_id FROM publishers
WHERE pub_name LIKE '%bo%';
```

### *g)* Nome das editoras que têm pelo menos uma publicação do tipo ‘Business’; 

```
SELECT publishers.pub_name, publishers.pub_id, titles.title  FROM publishers, titles
WHERE titles.type = 'Business' AND publishers.pub_id=titles.pub_id;

*Outra forma de ser Feito*

SELECT DISTINCT publishers.pub_name 
FROM publishers JOIN titles ON publishers.pub_id = titles.pub_id
WHERE titles.type='Business';
```

### *h)* Número total de vendas de cada editora; 

```
SELECT publishers.pub_name, publishers.pub_id, SUM(sales.qty)AS total_sales  FROM publishers, sales
GROUP BY publishers.pub_name, publishers.pub_id;
```

### *i)* Número total de vendas de cada editora agrupado por título; 

```
SELECT DISTINCT pub_name, title, SUM(ytd_sales)AS total_sales  
FROM (publishers JOIN titles ON publishers.pub_id = titles.pub_id)
GROUP BY pub_name, title
ORDER BY pub_name ASC; 
```

### *j)* Nome dos títulos vendidos pela loja ‘Bookbeat’; 

```
SELECT DISTINCT stor_name, title
FROM stores, titles
WHERE stor_name='Bookbeat';
```

### *k)* Nome de autores que tenham publicações de tipos diferentes; 

```
SELECT DISTINCT au_lname, au_fname, titles.type
FROM authors JOIN titleauthor ON authors.au_id = titleauthor.au_id
JOIN titles ON titleauthor.title_id=titles.title_id;
```

### *l)* Para os títulos, obter o preço médio e o número total de vendas agrupado por tipo (type) e editora (pub_id);

```
SELECT DISTINCT type, pub_id, AVG(price) AS preco_medio, SUM(qty) AS total_vendas
FROM titles JOIN sales ON titles.title_id = sales.title_id
GROUP BY type, pub_id;
```

### *m)* Obter o(s) tipo(s) de título(s) para o(s) qual(is) o máximo de dinheiro “à cabeça” (advance) é uma vez e meia superior à média do grupo (tipo);

```
SELECT type
FROM titles
GROUP BY type
HAVING MAX(advance) >= 1.5 * AVG(advance);
```

### *n)* Obter, para cada título, nome dos autores e valor arrecadado por estes com a sua venda;

```
SELECT DISTINCT title, au_lname, au_fname, SUM(royalty*price*ytd_sales*royaltyper / 10000) AS total_ganho
FROM titles JOIN titleauthor ON titles.title_id=titleauthor.title_id 
JOIN authors ON titleauthor.au_id=authors.au_id
GROUP BY title, au_lname, au_fname;
```

### *o)* Obter uma lista que incluía o número de vendas de um título (ytd_sales), o seu nome, a faturação total, o valor da faturação relativa aos autores e o valor da faturação relativa à editora;

```
SELECT ytd_sales, title, 
		SUM(price*ytd_sales) AS faturacao_total, 
		SUM(price*ytd_sales * (1-royalty/100)) AS faturacao_editora,
		SUM(royalty*price*ytd_sales*royaltyper / 10000) AS faturacao_autor
FROM titles JOIN titleauthor ON titles.title_id=titleauthor.title_id 
JOIN publishers ON titles.pub_id=publishers.pub_id
GROUP BY title, ytd_sales;
```

### *p)* Obter uma lista que incluía o número de vendas de um título (ytd_sales), o seu nome, o nome de cada autor, o valor da faturação de cada autor e o valor da faturação relativa à editora;

```
SELECT ytd_sales, title, au_lname, au_fname, 
		SUM(price*ytd_sales) AS faturacao_total, 
		SUM(price*ytd_sales * (1-royalty/100)) AS faturacao_editora,
		SUM(royalty*price*ytd_sales*royaltyper / 10000) AS faturacao_autor
FROM titles JOIN titleauthor ON titles.title_id=titleauthor.title_id 
JOIN publishers ON titles.pub_id=publishers.pub_id
JOIN authors ON titleauthor.au_id=authors.au_id
GROUP BY title, ytd_sales, au_lname, au_fname;
```

### *q)* Lista de lojas que venderam pelo menos um exemplar de todos os livros;

```
SELECT stor_id, COUNT(DISTINCT title_id) AS unique_titles
FROM sales
GROUP BY stor_id
HAVING COUNT(DISTINCT title_id) = (SELECT COUNT(DISTINCT title_id) FROM titles);
```

### *r)* Lista de lojas que venderam mais livros do que a média de todas as lojas;

```
WITH store_sales AS (
    SELECT stor_id, SUM(QTY) AS total_sold
    FROM sales
    GROUP BY stor_id
)

SELECT stor_id, SUM(qty) as total_sold FROM sales
GROUP BY stor_id
HAVING SUM(qty) > (SELECT AVG(total_sold) FROM store_sales);
```

### *s)* Nome dos títulos que nunca foram vendidos na loja “Bookbeat”;

```
SELECT t.title
FROM titles AS t
WHERE t.title_id NOT IN (
    SELECT s.title_id
    FROM sales AS s
    JOIN stores st ON s.stor_id = st.stor_id
    WHERE st.stor_name = 'Bookbeat');
```

### *t)* Para cada editora, a lista de todas as lojas que nunca venderam títulos dessa editora; 

```
WITH store_titles AS (
    SELECT sales.stor_id, titles.title_id, pub_id, stor_name FROM stores
    JOIN sales ON stores.stor_id = sales.stor_id
    JOIN titles ON sales.title_id = titles.title_id
)

SELECT publishers.pub_id, pub_name, stor_id, stor_name
FROM publishers
LEFT OUTER JOIN store_titles ON store_titles.pub_id = publishers.pub_id;
```

## Problema 6.2

### ​5.1

#### a) SQL DDL Script
 
[a) SQL DDL File](aula6.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_1_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT P.Pname, E.Ssn, E.Fname, E.Minit, E.Lname
FROM project P
JOIN works_on W ON P.Pnumber = W.Pno
JOIN employee E ON W.Essn = E.Ssn;
```

##### *b)* 

```
SELECT E.Fname, E.Minit, E.Lname
FROM employee E
JOIN employee S ON E.Super_ssn = S.Ssn
WHERE S.Fname = 'Carlos' AND S.Minit = 'D' AND S.Lname = 'Gomes';
```

##### *c)* 

```
SELECT P.Pname, SUM(W.Hours) AS Total_Hours
FROM project P
JOIN works_on W ON P.Pnumber = W.Pno
GROUP BY P.Pname;
```

##### *d)* 

```
SELECT E.Ssn AS Essn, W.Pno, W.Hours
FROM employee E
JOIN works_on W ON E.Ssn = W.Essn
JOIN project P ON W.Pno = P.Pnumber
WHERE E.Dno = 3 AND P.Pname = 'Aveiro Digital' AND W.Hours > 20;
```

##### *e)* 

```
SELECT Fname, Minit, Lname
FROM employee
WHERE Ssn NOT IN (SELECT Essn FROM works_on);
```

##### *f)* 

```
SELECT D.Dname, AVG(E.Salary) AS media_salario
FROM employee E
JOIN department D ON E.Dno = D.Dnumber
WHERE E.Sex = 'F'
GROUP BY D.Dname;
```

##### *g)* 

```
SELECT E.Fname, E.Minit, E.Lname
FROM employee E
JOIN (
    SELECT Essn, COUNT(*) AS NumDependentes
    FROM dependent
    GROUP BY Essn
    HAVING COUNT(*) > 2
) D ON E.Ssn = D.Essn;
```

##### *h)* 

```
SELECT E.Fname, E.Minit, E.Lname
FROM employee E
JOIN department D ON E.Ssn = D.Mgr_ssn
WHERE E.Ssn NOT IN (
    SELECT E2.Ssn
    FROM employee E2
    JOIN department D2 ON E2.Ssn = D2.Mgr_ssn
    JOIN dependent Dep ON E2.Ssn = Dep.Essn
);
```

##### *i)* 

```
SELECT E.Ssn, E.Fname, E.Minit, E.Lname, E.Address
FROM project P
JOIN works_on W ON P.Pnumber = W.Pno
JOIN employee E ON W.Essn = E.Ssn
JOIN department D ON E.Dno = D.Dnumber
JOIN dept_locations DL ON D.Dnumber = DL.Dnumber
WHERE DL.Dlocation <> 'Aveiro'
  AND P.Plocation = 'Aveiro';
```

### 5.2

#### a) SQL DDL Script
 
[a) SQL DDL File](exercicio_6_2_2_.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_2_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT f.nif, f.nome
FROM fornecedor f
WHERE f.nif NOT IN (
    SELECT e.fornecedor
    FROM encomenda e
);
```

##### *b)* 

```
SELECT AVG(unidades) AS Média_Stock
FROM produto;
```


##### *c)* 

```
WITH T1 AS (
    SELECT numEnc, COUNT(codProd) AS NumProdutos
    FROM item
    GROUP BY numEnc
)
SELECT AVG(CAST(NumProdutos AS FLOAT)) AS Média_Produtos
FROM T1;
```


##### *d)* 

```
SELECT f.nif, f.nome, SUM(i.unidades) AS Total_Stock
FROM fornecedor f
JOIN encomenda e ON f.nif = e.fornecedor
JOIN item i ON e.numero = i.numEnc
GROUP BY f.nif, f.nome;
```

### 5.3

#### a) SQL DDL Script
 
[a) SQL DDL File](exercicio_6_2_3.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_3_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT p.numUtente, p.nome
FROM paciente p
LEFT JOIN prescricao pr ON p.numUtente = pr.numUtente
WHERE pr.numPresc IS NULL;
```

##### *b)* 

```
SELECT m.especialidade, COUNT(*) AS numero_prescricoes
FROM medico m
JOIN prescricao pr ON m.numSNS = pr.numMedico
GROUP BY m.especialidade;
```


##### *c)* 

```
SELECT f.nome, COUNT(pr.numPresc) AS prescricoes_processadas
FROM farmacia f
JOIN prescricao pr ON f.nome = pr.farmacia
GROUP BY f.nome;
```


##### *d)* 

```
SELECT nome
FROM farmaco
WHERE numRegFarm = 906
EXCEPT
SELECT pf.nomeFarmaco
FROM presc_farmaco pf
WHERE numRegFarm = 906;
```

##### *e)* 

```
SELECT pfarm.nome AS farmacia, ff.nome AS farmaceutica, COUNT(ff.nome) AS vendas
FROM presc_farmaco pf
JOIN prescricao pr ON pf.numPresc = pr.numPresc
JOIN farmacia pfarm ON pr.farmacia = pfarm.nome
JOIN farmaceutica ff ON pf.numRegFarm = ff.numReg
GROUP BY pfarm.nome, ff.nome;
```

##### *f)* 

```
SELECT p.nome AS paciente, COUNT(DISTINCT m.nome) AS num_medicos
FROM prescricao pr
JOIN paciente p ON pr.numUtente = p.numUtente
JOIN medico m ON pr.numMedico = m.numSNS
GROUP BY p.nome;
```
