from faker import Faker
import pandas as pd
import numpy as np


fake = Faker()
info={
    "names" : [fake.name() for x in range(100)],
    "address" : [fake.address() for x in range (100)],
    "email" : [fake.email() for x in range(100)],
    "ages" : np.random.randint(20,60,100),
    "incomes" : np.random.randint(30000,100000,100)
}

data = pd.DataFrame(info)

print(data.head(10))