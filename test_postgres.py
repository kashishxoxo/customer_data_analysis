import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:kashdobrev@localhost:5432/customer_behaviour"
)
df = pd.read_csv(r"C:\Users\aditi\OneDrive\Desktop\project\cleaned_customer.csv")

df.to_sql(
    'customer_data',
    engine,
    if_exists="replace",
    index=False
)
print("Dataset uploaded")