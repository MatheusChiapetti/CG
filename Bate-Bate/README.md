<h1>Projeto 'Bate-Bate'.</h1>

Código em python orientado a objetos, com três classes, que realiza uma ação semelhante ao logo do DVD batendo nos cantos da tela. 

Abaixo, a imagem demonstra o diagrama UML das classes do projeto 'Bate-Bate'. Na sequência, são explicados os atributos e métodos:

![image](https://github.com/MatheusChiapetti/CG/assets/110207330/5647675b-2946-48da-a2a5-8f1f2081c57d)

<h3>Classe 'MovendoTexto':</h3>

- Os atributos da classe 'MovendoTexto' são: self, texto, fonte_tamanho, largura e altura.

- A classe 'MovendoTexto' apresenta os seguintes métodos:
  - __init__: utilizado para inicilizar os atributos da classe.
  - gerar_numero_nao_zero: utilizado para gerar um número que não seja 0, dentro do intervalo de -1 até 1.
  - move: utilizado para mover o objeto pela tela. Aqui realiza-se as validações para que o texto não saia dos limites/bordas da tela.
  - change_color: utilizado para sortear uma nova cor para o objeto dentro do expectro RGB toda vez que ele se choca com uma das paredes da tela (Superior, Inferior, Esquerda ou Direita).
  - draw: o método serve para desenhar o objeto na tela, levando-se em conta as mudanças e atualizações feitas pelos outros métodos da classe. 

<h3>Classe 'Game':</h3>
- Os atributos da classe 'Game' são os mesmos da classe 'MovendoTexto', devido à relação de hierarquia da orientação à objetos que foi aplicada ao projeto.

- A classe 'Game' apresenta os seguintes métodos:
  - __init__: utilizado para inicilizar os atributos da classe.
  - run: utilizado para executar o jogo. Esse método será chamado/acionado pelo 'main' ao criar um objeto do tipo 'Game'.

<h3>Classe 'main':</h3>

- Os atributos da classe 'main' são os mesmos da classe 'Game', que por sua vez são os mesmos da classe 'MovendoTexto', devido à relação de hierarquia da orientação à objetos que foi aplicada ao projeto.

- A classe 'main' apresenta apenas um método, sendo ele o '__name__', utilizado para executar o jogo.

- Observa-se que o 'main' é uma classe de inicialização, utilizada para melhor organizar o código e instanciar um objeto da classe 'Game'.
