# BD: Guião 5


## ​Problema 5.1
 
### *a)*

```
π Pname, Ssn, Fname, Minit, Lname (project ⨝ Pnumber=Pno (works_on ⨝ Essn=Ssn employee))
```


### *b)* 

```
π Fname, Minit, Lname (employee ⨝ (Super_ssn=supervisor.Ssn) (
ρ supervisor (π Ssn  (σ Fname='Carlos' ∧ Minit='D' ∧ Lname='Gomes' (employee)))))
```


### *c)* 

```
γ Pname;sum(Hours)→Total_Hours (project ⋈ Pnumber=Pno works_on)
```


### *d)* 

```
σ Hours > 20 (
ρ Essn←Ssn (σ Dno=3 (employee)) 
⨝ works_on
⨝ ρ Pno←Pnumber (σ Pname = 'Aveiro Digital' (project)))
```


### *e)* 

```
(π Fname, Minit, Lname (employee)) - (π Fname, Minit, Lname (employee ⨝ Ssn=Essn works_on))
```


### *f)* 

```
γ Dname;avg(Salary) -> media_salario ((σ Sex='F' (employee)) ⨝ Dno=Dnumber department)
```


### *g)* 

```
π Fname, Minit, Lname (
(σ NumDependentes>2 (γ Essn; count(*)→NumDependentes (dependent)))
⋈ Ssn=Essn employee)
```


### *h)* 

```
π Fname, Minit, Lname (
(π Ssn, Fname, Minit, Lname (employee ⋈ Ssn=Mgr_ssn department))
-
(π Ssn, Fname, Minit, Lname ((employee ⋈ Ssn=Mgr_ssn department) ⋈ Ssn=Essn dependent)))
```


### *i)* 

```
π Ssn, Fname, Minit, Lname, Address (
σ dept_location.Dlocation ≠ 'Aveiro' ∧ project.Plocation = 'Aveiro' (
(project ⨝ works_on ⨝ employee) ⨝ dept_location ⨝ department))
```


## ​Problema 5.2

### *a)*

```
π nif, nome (fornecedor)
−
π nif, nome (fornecedor ⋈ nif encomenda)
```

### *b)* 

```
γ código, nome; AVG(stock) → Média_Stock (produto)
```


### *c)* 

```
T1 ← γ númeroEncomenda; COUNT(código) → NumProdutos (produto)
γ ; AVG(NumProdutos) → Média_Produtos (T1)
```


### *d)* 

```
γ fornecedor.nif, fornecedor.nome; SUM(produto.stock) → Total_Stock
(fornecedor ⋈ fornecedor.nif = encomenda.nifFornecedor 
⋈ encomenda.numero = produto.numeroEncomenda)
```


## ​Problema 5.3

### *a)*

```
π numUtente,nome (σ numPresc = null (paciente ⟕ prescricao))
```

### *b)* 

```
medico_prescricao = medico ⨝numSNS=numMedico prescricao

γ especialidade;count(especialidade)->numero_prescricoes (medico_prescricao)
```


### *c)* 

```
prescricao_farmacia = farmacia ⨝nome=farmacia prescricao

γ nome;count(numPresc)->prescricoes_processadas (prescricao_farmacia)
```


### *d)* 

```
todos_farmacos_famacia906 = π nome (σ numRegFarm=906 (farmaco))

farmacos_farmacia906 = π presc_farmaco.nomeFarmaco (σ numRegFarm=906 (presc_farmaco))

todos_farmacos_famacia906-farmacos_farmacia906
```

### *e)* 

```
prescricao_farmacia = farmacia ⨝nome=farmacia prescricao

farmaceutica_farmaco_farmacia = π presc_farmaco.numPresc, numRegFarm, nomeFarmaco, nome (presc_farmaco ⨝prescricao.numPresc=presc_farmaco.numPresc (prescricao_farmacia))

nomeFarmaceutica_farmaco_farmacia = π presc_farmaco.numPresc, farmaceutica.nome, nomeFarmaco, farmacia.nome (farmaceutica ⨝numReg=numRegFarm farmaceutica_farmaco_farmacia)

γ farmacia.nome,farmaceutica.nome;count(farmaceutica.nome)->vendas (nomeFarmaceutica_farmaco_farmacia)
```

### *f)* 

```
prescricao_paciente = prescricao ⨝prescricao.numUtente=paciente.numUtente paciente

medico_paciente = π numSNS,medico.nome,paciente.nome (medico ⨝numSNS=numMedico (prescricao_paciente))

γ paciente.nome;count(medico.nome)->num_medicos (medico_paciente)
```
