import json
from pathlib import Path
import pdfplumber


CAMINHO_PDF = "relatorio_ferias.pdf"


def extrair_dados_pdf(caminho):
    funcionarios = []

    if not Path(caminho).exists():
        return {"erro": f"O arquivo '{caminho}' não foi encontrado."}

    with pdfplumber.open(caminho) as pdf:
        for page in pdf.pages:
            tabela = page.extract_table()
            if tabela:
               
                for linha in tabela[1:]:
                    if linha and len(linha) >= 3:
                        nome = linha[0].strip() if linha[0] else ""
                        email = linha[1].strip() if linha[1] else ""
                        data_retorno = linha[2].strip() if linha[2] else ""

                       
                        if nome and email and data_retorno:
                            funcionarios.append(
                                {
                                    "nome": nome,
                                    "email": email,
                                    "data_retorno": data_retorno,
                                }
                            )

    return funcionarios


if __name__ == "__main__":
    
    dados = extrair_dados_pdf(CAMINHO_PDF)

    print(json.dumps(dados))