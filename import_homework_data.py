#!/usr/bin/env python
# coding: utf-8

"""
Importa i dataset da homework.ipynb a PostgreSQL
"""

import pandas as pd
from sqlalchemy import create_engine, text
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
def import_homework_data(pg_user, pg_pass, pg_host, pg_port, pg_db):
    """Importa green_tripdata e taxi_zone_lookup a PostgreSQL"""
    
    # Connessione al database
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    # 1. Importa green_tripdata_2025
    click.echo("📥 Download green_tripdata_2025...")
    try:
        green_tripdata_2025 = pd.read_parquet(
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
        )
        click.echo(f"✓ Dataset caricato: {len(green_tripdata_2025)} righe")
        
        click.echo("📤 Inserisco in PostgreSQL (tabella: green_tripdata)...")
        green_tripdata_2025.to_sql(
            name='green_tripdata',
            con=engine,
            if_exists='replace',  # 'replace' sovrascrive, 'append' aggiunge
            index=False,
            chunksize=10000
        )
        click.echo("✓ green_tripdata importato con successo!")
    except Exception as e:
        click.echo(f"✗ Errore nell'importazione di green_tripdata: {e}", err=True)
        raise
    
    # 2. Importa taxi_zone_lookup
    click.echo("\n📥 Download taxi_zone_lookup...")
    try:
        taxi_zone_lookup = pd.read_csv(
            'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
        )
        click.echo(f"✓ Dataset caricato: {len(taxi_zone_lookup)} righe")
        
        click.echo("📤 Inserisco in PostgreSQL (tabella: taxi_zone_lookup)...")
        taxi_zone_lookup.to_sql(
            name='taxi_zone_lookup',
            con=engine,
            if_exists='replace',
            index=False
        )
        click.echo("✓ taxi_zone_lookup importato con successo!")
    except Exception as e:
        click.echo(f"✗ Errore nell'importazione di taxi_zone_lookup: {e}", err=True)
        raise
    
    # 3. Verifica l'importazione
    click.echo("\n📊 Verifica dell'importazione...")
    try:
        with engine.connect() as conn:
            # Check tabelle e righe
            result_green = conn.execute(text("SELECT COUNT(*) FROM green_tripdata"))
            count_green = result_green.scalar()
            
            result_taxi = conn.execute(text("SELECT COUNT(*) FROM taxi_zone_lookup"))
            count_taxi = result_taxi.scalar()
            
            click.echo(f"✓ green_tripdata: {count_green} righe")
            click.echo(f"✓ taxi_zone_lookup: {count_taxi} righe")
    except Exception as e:
        click.echo(f"✗ Errore nella verifica: {e}", err=True)
    
    click.echo("\n✨ Importazione completata!")


if __name__ == '__main__':
    import_homework_data()
