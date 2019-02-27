import pandas as pd
import pathlib

import db_settings as db_settings

if __name__ == "__main__":
    # PART 1: create schema & table
    db = db_settings.Database()
    table = 'Haha'
    db.run_sql_commands([
        ('''CREATE TABLE Countries (
            id INTEGER PRIMARY KEY,
            CountryCode TEXT,
            EnglishName TEXT,
            Region TEXT,
            Population INTEGER,
            Area REAL
        );
        ''',),
    ])
    db.run_sql_commands([
        ('''CREATE TABLE ChocolateBars (
            id INTEGER PRIMARY KEY,
            Company TEXT,
            SpecificBeanBarName TEXT,
            ReviewDate TEXT,
            CocoaPercent REAL,
            CompanyCountry INTEGER,
            Rating REAL,
            FOREIGN KEY (CompanyCountry) REFERENCES Countries(id)
        );
        ''',),
    ])

    # PART 0: read in data
    country_df = pd.read_json("countries.json")
    cacao_df = pd.read_csv("flavors_of_cacao_cleaned.csv")

    # PART 2: insert all data in the database
    countries_columns_lookup = {
        'alpha3Code': 'CountryCode',
        'name': 'EnglishName',
        'region': 'Region',
        'population': 'Population',
        'area': 'Area',
    }
    country_df = country_df[countries_columns_lookup.keys()]
    db.run_sql_command_many_data('''INSERT INTO Countries ({}) VALUES ({});'''.format(
            ','.join(countries_columns_lookup.values()),
            ','.join(['?'] * len(countries_columns_lookup))
        ),
        [tuple(row) for row in country_df.values]
    )

    chocolate_bars_columns_lookup = {
        'Company': 'Company',
        'SpecificBeanBarName': 'SpecificBeanBarName',
        'ReviewDate': 'ReviewDate',
        'CocoaPercent': 'CocoaPercent',
        'Rating': 'Rating',
    }
    chocolate_bars_fk_columns_lookup = {
        'CompanyLocation': {
            'foreignKeyFieldName': 'CompanyCountry',
            'referenceTable': 'Countries',
            'referenceFieldName': 'EnglishName',
        },
    }
    cacao_df = cacao_df[
        list(chocolate_bars_columns_lookup.keys()) + 
        list(chocolate_bars_fk_columns_lookup.keys())
    ]
    db.run_sql_command_many_data('''INSERT INTO ChocolateBars ({},{}) VALUES (
                {},
                {}
            );'''.format(
            # regular field names
            ','.join(chocolate_bars_columns_lookup.values()),
            # foreign key field names
            ','.join([
                dbFieldInfo['foreignKeyFieldName'] for dbFieldInfo in chocolate_bars_fk_columns_lookup.values()
            ]),

            # regular field placeholders
            ','.join(
                ['?'] * len(chocolate_bars_columns_lookup)
            ),
            # foreign key field sub queries
            ','.join(
                '(SELECT id FROM {} WHERE {}=?)'.format(
                    dbFieldInfo['referenceTable'],
                    dbFieldInfo['referenceFieldName'],
                ) for dbFieldInfo in chocolate_bars_fk_columns_lookup.values()
            )
        ),
        [tuple(row) for row in cacao_df.values]
    )

