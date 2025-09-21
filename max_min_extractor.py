import pandas as pd
import numpy as np

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :9].dropna(how='all')

# ✅ Comparacion con la respuesta esperada
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    #comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    comparison = pd.DataFrame(df.values == test.values)
    #comparison.columns = [f'Match{i+1}' for i in range(comparison.shape[1])]
    comparison.columns = [f'Match{i+1}' for i in range(comparison.shape[1])]
    return pd.concat([df_actual, df_expected, comparison], axis=1)


# 🔄 Transformar a formato largo
df_long = df_input.melt(id_vars='Name', var_name='Year', value_name='Value')

# 🎯 Filtrar valores máximos y mínimos
max_rows = df_long[df_long['Value'] == df_long['Value'].max()].copy()
min_rows = df_long[df_long['Value'] == df_long['Value'].min()].copy()

# 🧙‍♂️ Construir tabla final
output = []

for i, row in enumerate(max_rows.itertuples(index=False)):
    label = 'Max' if i == 0 else np.nan
    output.append([label, row.Name, row.Year])

# 🔀 Ordenar los mínimos por nombre
min_rows_sorted = min_rows.sort_values(by='Name').reset_index(drop=True)

for i, row in enumerate(min_rows_sorted.itertuples(index=False)):
    label = 'Min' if i == 0 else np.nan
    output.append([label, row.Name, row.Year])

test = df_raw.iloc[:, 10:].dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
# 📊 Convertir a DataFrame
df = pd.DataFrame(output, columns=['Category', 'Name', 'Year']).fillna('').reset_index(drop=True)
df['Year'] = df['Year'].astype(int)

test = df_raw.iloc[:, 10:].dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
df_final = compare_with_expected(df, test)

print(df_final)
