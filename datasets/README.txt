Título da proposta: Estabilidade e variabilidade da expressão gênica específicas do sexo e da região cerebral durante o envelhecimento humano: um estudo transcriptômico com dados GTEx
-------------------------------------------------

Descricao:
cerebro é composto por diversas regiões. Nos arquivos gz, estão 13 regioes do cerebro equivalente a 1 arquivo pra cada regiao. Cada arquivo possui dados normalizados em TPM, com uma quantidade de amostras sequenciadas por rna-seq. 
-------------------------------------------------

Hipótese central
A variabilidade da expressão gênica entre indivíduos não é distribuída uniformemente pelo cérebro humano. Diferentes regiões apresentam níveis próprios de estabilidade transcriptômica, e esses padrões podem se modificar com o envelhecimento de maneira distinta entre homens e mulheres.
-------------------------------------------------

Objetivos específicos
1. Identificar os genes com maior e menor variabilidade interindividual (genes que variam menos entre as pessoas considerando as regioes do cerebro) nas diferentes regiões cerebrais.
2. Determinar se a idade e o sexo estão associados a diferenças na expressão média e na variabilidade dos genes.
3. Comparar a heterogeneidade transcriptômica entre regiões cerebrais, identificando regiões com padrões mais estáveis ou mais variáveis (quais regioes mudam menos ou mais de expressao durante o envelhecimento, considerando todos juntos, e entre sexos).
4. Desenvolver e comparar modelos de machine learning capazes de classificar a região cerebral a partir dos perfis de expressão gênica, investigando o efeito do sexo e da idade sobre o desempenho e as características selecionadas.
-------------------------------------------------

Descrição dos arquivos:

-arquivo GTEx_Analysis_v11_Annotations_SubjectPhenotypesDS.txt:
SUBJID: codigo da amostra que aparece nos arquivos TPM de expressão
SEX: sexo m=1, f=2
AGE:intervalo de idade da amostra, não é valor exato
DTHHRDY:causa da morte (irrelevante pro estudo)

-gene_tpm_adult_gtex_v11_brain_amygdala.gct.gz:
Name: código da feature emsenbl
Description: nome do gene equivalente ao ensembl
GTEX-XXXXX: código da amostra, e pra descobrir a idade basta cruzar com o arquivo acima





-------------------------------------------------
Fonte dos dados (GTEx Portal, release v11):
https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression
Arquivos de anotacao de fenotipos (SubjectPhenotypesDS / DD):
https://gtexportal.org/home/downloads/adult-gtex/metadata
