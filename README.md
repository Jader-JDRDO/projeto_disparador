🏖️ Alerta de Retorno de Férias & Redefinição de Senha

Sistema de automação desenhado para identificar colaboradores que estão prestes a retornar do período de férias e disparar um e-mail de lembrete com 1 dia de antecedência, instruindo-os sobre a atualização da senha temporária de rede/e-mail.


🛠️ Arquitetura do Projeto

A solução utiliza uma abordagem híbrida (Python + n8n):

1. Leitura e Extração (Python): O script em Python lê o relatório mensal em PDF, extrai os dados das tabelas e transforma os registros em uma estrutura JSON tratada.
2. Orquestração e Disparo (n8n): O n8n executa o agendamento diário (Cron), recebe o JSON, valida a data de retorno (filtrando quem volta exatamente no dia seguinte) e dispara o e-mail personalizado através da API do provedor (Gmail / Outlook / SMTP).



📁 Estrutura de Arquivos

1- extrair_pdf.py       # Script Python responsável por ler o PDF e gerar o JSON
2- relatorio_ferias.pdf # Arquivo PDF de entrada (Relatório do RH)
3- workflow_n8n.json    # Fluxo exportado do n8n para importação direta
