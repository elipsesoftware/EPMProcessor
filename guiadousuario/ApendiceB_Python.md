# Apêndice B - Dicas de Python

*[Retornar ao menu](README.md)*

## Acessando Packages Globais

É possível criar métodos em **Packages** acessíveis por outros **Packages** dentro do **EPM Processor**. Para isto é preciso seguir um dos métodos a seguir.

> + Executar o comando `import` do **Package** dentro do método decorado, conforme o exemplo a seguir.

```python

import epmprocessor as epr

@epr.applicationMethod('MyMethod')
def my_method(session, param1):
    import mypackage
    ...

```

> + Executar o comando `append` do local onde o **EPM Processor** salva os **Packages**, conforme o exemplo a seguir.

```python

import epmprocessor as epr

import sys

sys.path.append('C:\ProgramData\Elipse Software\EpmProcessor\EpmProcessorPyEngine\Package')

import mypackage

@epr.applicationMethod('MyMethod')
def my_method(session, param1):
    ...


```

## Convertendo para Pandas

Para converter um objeto **ndarray** do **EPM** para o **DataFrame** do **Pandas**, execute o exemplo a seguir.

```python
import pandas as pd

def epm2pandas(epmdata):
    """Transform epm ndarray(value, timestamp, quality) in pandas dataframe"""

    df = pd.DataFrame(
            {'Value': epmdata['Value'].tolist(),
             'Timestamp': epmdata['Timestamp'].tolist(),
             'Quality': epmdata['Quality'].tolist()}
            )

    return df
```
