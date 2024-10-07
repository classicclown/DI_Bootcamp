from restcountries import RestCountryApiV2 as rapi
import psycopg2
import requests
import json

def db_connect():
    print('Connecting..')
    conn = psycopg2.connect(
                    database='Web API to DB',
                    user='postgres',
                    password='password',
                    host='localhost',
                    port=5431,
                    )
    print('Connected')
    cursor=conn.cursor()
    return conn,cursor
  
              

def get_countries(names):
    countries=[]
    response_API = requests.get(f'https://restcountries.com/v3.1/all?fields=name,capital,population,flag,subregion')
    
    if response_API.status_code == 200:

        data = response_API.json()
        for country_info in data:
            country_name = country_info.get('name', {}).get('common', 'Unknown')
            if country_name in names:
                capital = country_info.get('capital', ['Unknown'])[0]
                population = country_info.get('population', 'Unknown')
                flag= country_info.get('flag', 'Unknown')
                subregion=country_info.get('subregion','Unkown')

                countries.append({
                    'Name':country_name,
                    'Capital':capital,
                    'Population':population,
                    'Flag':flag,
                    'Subregion':subregion})
    else:
        print(f"Failed to fetch data for {name}, Status code: {response_API.status_code}")
    return countries

            
def write_to_db(conn,cursor,countries):
    for country in countries:
        query = f'INSERT INTO Countries (Name,Capital,Population,Flag,Subregion) VALUES (%s,%s,%s,%s,%s)'
        values = (country['Name'],country['Capital'],country['Population'],country['Flag'],country['Subregion'])

        try:
            cursor.execute(query,values)
            conn.commit()
            print("Inserted countries")
        except Exception as e:
            print(f'Error insertinf {country['Name']}: {e}')

def main():
    # conn,cursor=db_connect()
    country_names = ["South Africa", "Australia", "Thailand", "Bermuda", "Mexico", "Peru", "Canada", "Germany", "Ukraine", "Albania"]
    countries = get_countries(country_names)
    print(countries)
    # write_to_db(conn,cursor,countries)
    # cursor.close()
    # conn.close()


if __name__== '__main__':
    main()
