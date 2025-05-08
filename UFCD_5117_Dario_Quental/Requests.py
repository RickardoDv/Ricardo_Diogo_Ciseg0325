import requests

# URL fornecida
url = "https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx"
params = {
    "command": "_SelectAllSchedulesDataSetGivenByUserId",
    "oId": 7199,
    "idField": "DataValueField",
    "titleField": "DataTextField",
    "startDateField": "DataStartField",
    "endDateField": "DataEndField",
    "backgroundColorField": "",
    "textColorField": "textcolor",
    "eventColorField": "color",
    "description": "description",
    "picField": "pic",
    "urlField": "url",
    "start": 1747081259,
    "end": 1747004400,
    "_": 1746734789633
}

# Nome a procurar (case insensitive)
nome_procurado = "rogélio"

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    encontrados = []
    for item in data:
        # Verifica todas as strings no dicionário
        if any(nome_procurado in str(valor).lower() for valor in item.values()):
            encontrados.append(item)

    if encontrados:
        print(f"Foram encontrados {len(encontrados)} resultados com o nome '{nome_procurado}':\n")
        for e in encontrados:
            print(e)
    else:
        print(f"Nenhum resultado encontrado com o nome '{nome_procurado}'.")

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a URL:", e)
except ValueError:
    print("Resposta não é um JSON válido.")
