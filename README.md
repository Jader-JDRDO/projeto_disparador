🏖️ Alerta de Retorno de Férias & Redefinição de Senha

Sistema de automação desenhado para identificar colaboradores que estão prestes a retornar do período de férias e disparar um e-mail de lembrete com 1 dia de antecedência, orquestrando notificações preventivas tanto para a equipe de TI/Encarregado quanto para o próprio funcionário instruindo-os sobre a atualização da senha temporária de rede/e-mail.


🛠️ Arquitetura do Projeto

A solução utiliza uma abordagem híbrida (Python + n8n):

1. Leitura e Extração (Python): O script em Python lê o relatório mensal em PDF, extrai os dados das tabelas estruturando as informações necessárias para análise das datas de retorno e transforma os registros em um ETL para diagnosticar e enviar os emails após analise.

2. Orquestração e Notificações (n8n): 
- Alerta ao Encarregado de TI: Notifica previamente o responsável pela gestão de acessos sobre quais colaboradores retornam no dia seguinte. Isso permite que a senha seja convertida para o padrão a tempo e que a equipe esteja preparada caso o colaborador enfrente dificuldades no acesso.
- Envia um e-mail com 1 dia de antecedência lembrando o colaborador sobre o retorno e instruindo-o sobre o uso e redefinição da senha padrão corporativa.
  



📁 Estrutura de Arquivos

1- disparador.py #Script Python responsável por ler o PDF e gerar o JSON
2- relatorio_ferias.pdf #Arquivo PDF de entrada (Relatório emitido pelo RH)
3- Alerta.json #Fluxo exportado do n8n (Workflow de automação)
4- README.md #Documentação do projeto



