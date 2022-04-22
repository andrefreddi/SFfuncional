# Super Fatorial

#### Equipe: André Freddi e Willian Choaste

---

Vamos visualizar e editar executar o código vamos utilizar o Colab:

https://colab.research.google.com/drive/1NusWRfDC6_7p5gRjJXxcuU-tN-Z09Oun?usp=sharing


Primeiramente vamos rodar código que gera a tabela Hash Table.

![image](https://user-images.githubusercontent.com/52337680/164572027-68a4bb16-e17f-4b86-bef3-a6b30779ec4c.png)

Após isso vamos executar o código que calcula o fatorial, utilizando o Hash Table:

![image](https://user-images.githubusercontent.com/52337680/164573359-d2f694fa-e1fb-4bc0-95c9-97b77fdb223f.png)

Antes de partirmos aos testes, vamos entender o que nosso código faz:

Inicialmente temos as primeiras definições e nota-se que setamos a chave como 4, invés de utilizar o "input("Chave: ")" para o usuário digitar o valor, por quê? Bom para fins de testes e comparação de desempenho, em quanto o usuário não digitar o valor ele continua correndo o tempo.

![image](https://user-images.githubusercontent.com/52337680/164573990-f36fddde-5b7e-464a-956d-71809d1da0c0.png)

Aqui vamos definir o super fatorial da chave para a comparação com a HashTable.

Nosso “range:"ira retornar uma série numérica no intervalo.

E o "pow:" pega dois parâmetro e eleva o primeiro valor pelo segundo, calculando assim nosso Super Fatorial.

![image](https://user-images.githubusercontent.com/52337680/164574055-8a20305f-69e2-414f-9f4e-c4b3a46c3a1a.png)

Vamos verifica se o Super Fatorial da Chave está presente na HashTable.

SE NÃO estiver realiza o calulo e imprime este super fatorial.

SE SIM ele imprime o super fatorial na tela.

![image](https://user-images.githubusercontent.com/52337680/164575205-3c27b4ad-753a-44f2-a8e8-ab5c43c3b2ca.png)

E aqui temos os Prints do nosso código do Tempo de duração, O uso da CPU e Uso de Memoria RAM.

![image](https://user-images.githubusercontent.com/52337680/164575331-88c2825c-687a-4143-8ac1-95a0f9e24e9e.png)

## Vamos aos testes

Executando o código, e não tendo o valor na Tabela, ele ira calcular o Super fatorial pala primeira vez (Super fatorial de 4 = 288):

![image](https://user-images.githubusercontent.com/52337680/164575998-eb10995a-135d-4bb7-89b3-a2e4cf300029.png)

Se executarmos novamente com o valor do super fatorial já calculado, temos o resultado:

![image](https://user-images.githubusercontent.com/52337680/164576137-2d1f928a-628a-45b4-97a1-368ba287a087.png)





