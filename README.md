# Análise Exploratória de Dados - Titanic

**Aluno:** Cassiuscray Felipe dos Santos - Matrícula: 2024007815
**Aluno:** Bryan Luiz Veloso da Silva - Matrícula: 2024007753

# Como Executar
O projeto utiliza um ambiente virtual Conda para gerenciar as dependências (Pandas, Matplotlib, Seaborn). Para executar:

### 1- Abra o terminal e rode: git clone https://github.com/Felipe4702/DadosTitanic
### 2- Entre na pasta rodando: cd DadosTitanic
### 3- Crie o ambiente rodando: conda env create -f environment.yml
### 4- Depois ative o ambiente com: conda activate titanic
### 5- Para executar, use: python main.py

# Resultados e Interpretações

**1. Distribuição de Idade por Gênero e Classe Social**
* **Idade por Classe:** A 1ª classe abrigava os passageiros mais velhos do navio, com medianas acima dos 35 anos. Em contraste, a 3ª classe era composta majoritariamente por jovens, com a mediana de idades variando entre 20 e 25 anos.
* **Gênero:** Dentro de uma mesma classe social, os homens tendiam a ser ligeiramente mais velhos que as mulheres.
* **Dispersão:** Observa-se a presença de extremos (idosos) na 2ª e 3ª classes, indicando passageiros com idades muito acima do padrão esperado para aqueles grupos específicos.

**2. Taxa de Sobrevivência por Faixa Etária**
* **Prioridade de Resgate:** A regra histórica de "mulheres e crianças primeiro" reflete-se nos dados. O grupo de Crianças (0-12 anos) registrou a maior taxa proporcional de sobrevivência (aprox. 54%). Os Idosos (60+ anos) compõem o grupo com a menor chance de sobrevivência (aprox. 23%), seguidos pelos Adultos (37%).

**3. Relação entre Tarifa e Sobrevivência**
* **Correlação Positiva:** Existe uma correlação matemática direta entre o valor pago pelo bilhete e a sobrevivência do passageiro. 
* **Média de Valores:** A tarifa média do grupo que sobreviveu foi estatística e significativamente maior do que a tarifa média do grupo que não sobreviveu.
* **Conclusão:**  Segundo uma analise rapida dos dados, o fator socioeconômico foi determinante na tragédia. Passageiros com maior poder aquisitivo tiveram prioridade ou maior facilidade de acesso aos botes salva-vidas.
