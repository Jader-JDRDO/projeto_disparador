🏖️ Alerta de Retorno de Férias & Redefinição de Senha

Sistema de automação desenhado para identificar colaboradores que estão prestes a retornar do período de férias e disparar um e-mail de lembrete com 1 dia de antecedência, instruindo-os sobre a atualização da senha temporária de rede/e-mail.


🛠️ Arquitetura do Projeto

A solução utiliza uma abordagem híbrida (Python + n8n):

1. Leitura e Extração (Python): O script em Python lê o relatório mensal em PDF, extrai os dados das tabelas e transforma os registros em um ETL para diagnosticar e enviar os emails após analise.
2. Notificar o encarregado de mudar a senha do colaborador para a senha padrão, assim já ficando ciente que talvez o colaborar esqueça da senha padrão ou esqueça de trocar e já ter preparado previamente os dados para alteração do colaborar em questão.




📁 Estrutura de Arquivos

1- disparador.py       # Script Python responsável por ler o PDF e gerar o JSON
2- relatorio_ferias.pdf # Arquivo PDF de entrada (Relatório do RH)

