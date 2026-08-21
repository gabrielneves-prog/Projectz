import re
from pathlib import Path
from pypdf import PdfReader


def retornar_datas(texto: str):
    expressao = r"\d{2}/\d{2}/\d{4}"
    return re.findall(expressao, texto)


def retornar_vendas(produtos: list, texto: str):
    vendas = {}

    for produto in produtos:
        expressao = rf"({produto}):\s*(\d+)\s*unidades"
        resultados = re.findall(expressao, texto)

        soma = 0

        for resultado in resultados:
            soma += int(resultado[1])

        vendas[produto] = soma

    return vendas


# Localiza a pasta onde está o main.py
pasta_projeto = Path(__file__).parent

# Localiza o vendas.pdf na mesma pasta do main.py
arquivo_pdf = pasta_projeto / "vendas.pdf"

# Lê o PDF
vendas_relatorio = PdfReader(arquivo_pdf)

print(f"Número de páginas: {len(vendas_relatorio.pages)}")


# Extrai o texto de todas as páginas
texto_completo = ""

for pagina in vendas_relatorio.pages:
    texto = pagina.extract_text()

    if texto:
        texto_completo += texto


# Encontra as datas
datas = retornar_datas(texto_completo)


# Produtos que serão analisados
lista_produtos = ["Mouse", "Teclado"]

produtos = retornar_vendas(
    lista_produtos,
    texto_completo
)


# Cria o relatório
arquivo_txt = pasta_projeto / "resumo_vendas.txt"

with open(arquivo_txt, "w", encoding="utf-8") as arquivo:

    arquivo.write("RELATÓRIO DE VENDAS\n")
    arquivo.write("=" * 30)
    arquivo.write("\n\n")

    arquivo.write("DATAS ENCONTRADAS:\n")

    for data in datas:
        arquivo.write(f"{data}\n")

    arquivo.write("\nPRODUTOS:\n")

    for produto, qtd in produtos.items():
        arquivo.write(f"{produto}: {qtd} unidades\n")


print(f"Relatório criado com sucesso em:")
print(arquivo_txt)