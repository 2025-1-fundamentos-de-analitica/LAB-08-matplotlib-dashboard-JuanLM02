# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
 
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)

    # Leer datos
    df = pd.read_csv("files/input/shipping-data.csv")

    # Gráfico 1: shipping_per_warehouse.png
    shipping_per_warehouse = df.groupby("Warehouse_block")["ID"].count()
    plt.figure(figsize=(4,3))
    shipping_per_warehouse.plot(kind='bar', color='skyblue')
    plt.title('Shipping per Warehouse')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Number of Shipments')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/shipping_per_warehouse.png")
    plt.close()

    # Gráfico 2: mode_of_shipment.png
    plt.figure(figsize=(4,3))
    df['Mode_of_Shipment'].value_counts().plot.bar(color='lightgreen')
    plt.title('Mode of Shipment')
    plt.xlabel('Mode')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/mode_of_shipment.png")
    plt.close()

    # Gráfico 3: average_customer_rating.png
    plt.figure(figsize=(4,3))
    df['Customer_rating'].plot.hist(bins=5, color='salmon', rwidth=0.8)
    plt.title('Average Customer Rating')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/average_customer_rating.png")
    plt.close()

    # Gráfico 4: weight_distribution.png
    plt.figure(figsize=(4,3))
    df['Weight_in_gms'].plot.hist(bins=20, color='gold', rwidth=0.8)
    plt.title('Weight Distribution')
    plt.xlabel('Weight (gms)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/weight_distribution.png")
    plt.close()

    # Crear HTML index.html
    html = f"""
    <html>
    <head>
        <title>Shipping Dashboard</title>
        <style>
            body {{ font-family: Arial; }}
            .container {{ display: flex; flex-wrap: wrap; gap: 20px; }}
            .chart {{ flex: 1 1 45%; text-align: center; }}
            img {{ max-width: 100%; height: auto; border: 1px solid #ccc; }}
        </style>
    </head>
    <body>
        <h1>Shipping Dashboard</h1>
        <div class="container">
            <div class="chart">
                <h2>Shipping per Warehouse</h2>
                <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
            </div>
            <div class="chart">
                <h2>Mode of Shipment</h2>
                <img src="mode_of_shipment.png" alt="Mode of Shipment">
            </div>
            <div class="chart">
                <h2>Average Customer Rating</h2>
                <img src="average_customer_rating.png" alt="Average Customer Rating">
            </div>
            <div class="chart">
                <h2>Weight Distribution</h2>
                <img src="weight_distribution.png" alt="Weight Distribution">
            </div>
        </div>
    </body>
    </html>
    """

    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Dashboard creado en docs/index.html")