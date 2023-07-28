# simpleTESTS

SimpleTESTS é um projeto de teste unitário simples e fácil de usar, projetado para tornar a escrita e a execução de testes tão simples quanto possível. Ele usa um sistema de decoradores para marcar funções como testes e, em seguida, executa esses testes em threads separadas para maximizar a eficiência.

## Como usar

Para usar o simpleTESTS, você precisa seguir os seguintes passos:

1. Importe o decorador `test` e a função `runTests` do módulo `simpleTESTS` em seu arquivo de teste.

```python
from simpleTESTS import test, runTests
```
2. Use o decorador `test` para marcar uma função como um teste. O decorador `test` aceita um argumento: o valor esperado do teste.

```python
@test(expected='aaa')
def myTestFunction():
    return 'aaa'
```


3. Chame a função `runTests` no final do seu arquivo de teste. Esta função aceita dois argumentos: o conteúdo do arquivo de teste e o nome do arquivo de teste.



## Exemplo

Aqui está um exemplo de como usar o simpleTESTS para testar se duas URLs retornam o código de status HTTP 200.

```python
from main import test, runTests
import requests

@test(expected=200)
def privateData():
    return requests.get('http://127.0.0.1:8000/private/data').status_code

@test(expected=200)
def publicData():
    return requests.get('http://127.0.0.1:8000/public/data').status_code

if __name__ == 'main':
    content = open(file).read()
    runTests(content, name)
```
Neste exemplo, as funções `privateData` e `publicData` são marcadas como testes. Cada função faz uma solicitação GET para uma URL e retorna o código de status HTTP da resposta. O valor esperado para cada teste é 200, que é o código de status HTTP para uma resposta bem-sucedida.
