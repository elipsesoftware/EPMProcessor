# Apêndice A - Agregações

*[Retornar ao menu](menu.md)*

|Agregação|Descrição|
|---|---|
|**Interpolative**|Interpola os pontos consecutivos dos dados de um intervalo definido, segundo a amostragem especificada no campo **Sample Interval**. Para variáveis discretas, a interpolação apenas mantém o valor anterior até o seguinte. Para variáveis contínuas, a interpolação entre dois pontos consecutivos é linear|
|**Average**|Média aritmética, ou seja, a soma de todos os valores com qualidade boa do intervalo dividida pelo número de dados com qualidade boa|
|**TimeAverage**|Média ponderada pelo tempo, utilizando os dados interpolados linearmente|
|**Total**|Retorna o resultado do cálculo **TimeAverage &times; SampleInterval**|
|**MinimumActualTime**|Retorna o menor valor presente no intervalo especificado, utilizando a estampa de tempo de quando o valor ocorreu|
|**MaximumActualTime**|Retorna o maior valor presente no intervalo especificado, utilizando a estampa de tempo de quando o valor ocorreu|
|**Minimum**|Equivale ao campo **MinimumActualTime**, porém utiliza a estampa de tempo do início do intervalo ao invés de quando o valor efetivamente ocorreu|
|**Maximum**|Equivale ao campo **MaximumActualTime**, porém utiliza a estampa de tempo do início do intervalo ao invés de quando o valor efetivamente ocorreu|
|**Range**|Retorna a diferença entre o valor máximo e mínimo do intervalo especificado no campo **Sample Interval**. Se houver apenas um valor com qualidade boa no intervalo, retorna o valor 0 (zero)|
|**AnnotationCount**|Retorna o número de anotações inseridas na variável no intervalo especificado no campo **Sample Interval**|
|**Count**|Retorna o número total de dados com qualidade boa armazenados no intervalo especificado no campo **Sample Interval**|
|**DurationInStateZero**|Retorna o tempo transcorrido em milissegundos, dentro do intervalo especificado no campo **Sample Interval**, em que o estado do Tag era 0 (zero)|
|**DurationInStateNonZero**|Retorna o tempo transcorrido em milissegundos, dentro do intervalo especificado no campo **Sample Interval**, em que o estado do Tag era diferente de 0 (zero.||
|**NumberOfTransitions**|Retorna o número total de transições do valor da variável dentro do intervalo especificado nos campos **Sample Interval** e **Unit**|
|**Start**|Retorna o primeiro valor com qualidade boa encontrado no intervalo especificado no campo **Sample Interval** com a estampa de tempo em que ocorreu|
|**End**|Retorna o último valor com qualidade boa encontrado no intervalo especificado no campo **Sample Interval** com a estampa de tempo em que ocorreu|
|**Delta**|Retorna a diferença entre o primeiro e o último valor dentro do intervalo especificado no campo **Sample Interval** e que tenham qualidade boa. Corresponde ao resultado do cálculo **Delta &equals; End &minus; Start**|
|**DurationGood**|Retorna o tempo, em milissegundos, em que os dados estavam com qualidade boa no intervalo especificado no campo **Sample Interval**. A qualidade é definida a partir da qualidade dos dados do limite do intervalo|
|**DurationBad**|Retorna o tempo, em milissegundos, em que os dados estavam com qualidade ruim no intervalo especificado no campo **Sample Interval**. A qualidade é definida a partir da qualidade dos dados do limite do intervalo|
|**PercentGood**|Retorna o resultado do cálculo **PercentGood &equals; DurationGood &divide; SampleInterval &times; 100**|
|**PercentBad**|Retorna o resultado do cálculo **PercentBad &equals; DurationBad &divide; SampleInterval &times; 100**|
|**WorstQuality**|Retorna a pior qualidade dos dados presentes no intervalo especificado no campo **Sample Interval**. A qualidade **Bad** é pior que **Uncertain**, que por sua vez é pior que **Good**. A estampa de tempo sempre corresponde ao início do intervalo|

> + As agregações seguem o padrão **OPC UA**. Consulte a norma da *[OPC Foundation](https://www.opcfoundation.org)* para mais informações.
> + Todos os cálculos de agregações incluem a data e hora inicial mas excluem a data e hora final da consulta.
