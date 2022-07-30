from bs4 import BeautifulSoup
import requests
import json
import pandas


def propertyparser(results, region):
    aresults = []
    print(len(results["results"]))
    for json in results["results"]:
        # stringid = json.get("realEstate").get("id")
        stringid = json["realEstate"]["id"]
        price = json["realEstate"]["price"]["value"]
        bathrooms = json["realEstate"]["properties"][0]["bathrooms"]
        caption = json["realEstate"]["properties"][0]["caption"]
        category = json["realEstate"]["properties"][0]["category"]["name"]
        discription = json["realEstate"]["properties"][0]["description"]
        floor = json["realEstate"]["properties"][0]["floor"]
        if floor is not None:
            # floor.get("value")
            floor["value"]
        else:
            floor = "not assigned"

        rooms = json["realEstate"]["properties"][0]["rooms"]
        surface = json["realEstate"]["properties"][0]["surface"]
        lon = json["realEstate"]["properties"][0]["location"]["longitude"]
        lat = json["realEstate"]["properties"][0]["location"]["latitude"]
        marker = json["realEstate"]["properties"][0]["location"]["marker"]
        aphoto = []
        for photo in json["realEstate"]["properties"][0]["multimedia"]["photos"]:
            url = photo["urls"]["small"]
            aphoto.append(url)

        item = {
            "region": region,
            "id": stringid,
            "price": price,
            "bathrooms": bathrooms,
            "caption": caption,
            "category": category,
            "discription": discription,
            "floor": floor,
            "rooms": rooms,
            "surface": surface,
            "longitude": lon,
            "latitude": lat,
            "marker": marker,
            "photo": aphoto,
        }
        aresults.append(item)
        # print(item)
    return aresults


url1 = "https://www.immobiliare.it/api-next/search-list/real-estates/?fkRegione=tos&idProvincia=LU&idNazione=IT&idContratto=1&idCategoria=1&prezzoMinimo=10000&prezzoMassimo=26000&idTipologia[0]=7&idTipologia[1]=31&idTipologia[2]=11&idTipologia[3]=12&idTipologia[4]=13&idTipologia[5]=4&localiMinimo=3&localiMassimo=5&bagni=1&boxAuto[0]=4&cantina=1&noAste=1&__lang=en&pag=1&paramsCount=17&path=%2Fen%2Fsearch-list%2F"
url2 = "https://www.immobiliare.it/api-next/search-list/real-estates/?fkRegione=tos&idProvincia=PI&idNazione=IT&idContratto=1&idCategoria=1&prezzoMinimo=10000&prezzoMassimo=31000&idTipologia[0]=7&idTipologia[1]=31&idTipologia[2]=11&idTipologia[3]=12&idTipologia[4]=13&idTipologia[5]=4&localiMinimo=3&localiMassimo=5&bagni=1&boxAuto[0]=4&cantina=1&noAste=1&pag=1&paramsCount=17&path=%2Fen%2Fsearch-list%2F"
urlmany = "https://www.immobiliare.it/api-next/search-list/real-estates/?fkRegione=tos&idProvincia=PI&idNazione=IT&idContratto=1&idCategoria=1&prezzoMinimo=10000&prezzoMassimo=50000&idTipologia[0]=7&idTipologia[1]=31&idTipologia[2]=11&idTipologia[3]=12&idTipologia[4]=13&idTipologia[5]=4&localiMinimo=3&localiMassimo=5&bagni=1&boxAuto[0]=4&cantina=1&noAste=1&pag=1&paramsCount=17&path=%2Fen%2Fsearch-list%2F"

response = requests.get(urlmany)

a = propertyparser(response.json(), "TOSCANA")

df = pandas.DataFrame(a)
print(df)
