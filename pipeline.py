import requests
import pandas as pd
import sqlite3

def extract():
    print("Fetching data from API...")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

def transform(data):
    print("Transforming data...")
    df = pd.DataFrame(data)
    df = df[['id', 'title']]
    return df

def load(df):
    print("Loading data into database...")
    conn = sqlite3.connect("data.db")
    df.to_sql("posts", conn, if_exists="replace", index=False)
    conn.close()

def run_pipeline():
    data = extract()
    df = transform(data)
    load(df)
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()