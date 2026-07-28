from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pdfplumber
import pathlib


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "mrcartonrex@gmail.com"
SENHA = "414303Jdrd@"


amanha = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")

funcionarios_para_notificar = []

# 3. Ler o PDF e extrair os dados
with pdfplumber.open("relatorio_ferias.pdf") as pdf:
    for page in pdf.pages:
        tabela = page.extract_table()
        if tabela:
            for linha in tabela[1:]:  
                nome, email, data_retorno = linha[0], linha[1], linha[2]

                if data_retorno.strip() == amanha:
                    funcionarios_para_notificar.append(
                        {"nome": nome, "email": email}
                    )

# 4. Enviar os e-mails
if funcionarios_para_notificar:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, SENHA)

    for func in funcionarios_para_notificar:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = func["email"]
        msg[
            "Subject"
        ] = "⚠️ [Lembrete TI] Atualização de Senha - Retorno das Férias"

        corpo = f"""
        Olá, {func['nome']}!
        
        Lembrando que seu retorno das férias é amanhã ({amanha}).
        
        Durante o período de descanso, sua senha do e-mail corporativo foi convertida para a senha padrão temporária:
        🔑 Senha Temporária: SuaEmpresa@2026
        
        Por favor, redefina sua senha no primeiro acesso.
        
        Atenciosamente,
        Equipe de TI
        """
        pasta = pathlib.Path(r'assets')
        caminho = str(pasta.resolve())
        msg.Attachments.Add(caminho)
        msg.attach(MIMEText(corpo, "plain"))
        
        server.send_message(msg)
        

    server.quit()
    print(f"Sucesso: {len(funcionarios_para_notificar)} e-mails enviados.")
else:
    print("Nenhum funcionário retornando amanhã.")