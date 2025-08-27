from sql_connection import get_sql_connection

def get_all_products(connection):
   
    cursor = connection.cursor()
    query = ("select products.products_id, products.Name,products.uom_id,products.Price_per_unit,uom.uom_name "
    "from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit,uom_name) in cursor:
        response.append(
            {
                'products_id':product_id,
                'name':name,
                'uom_id':uom_id,
                'Price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )  
    return response

def insert_new_product(connection,products):
    cursor = connection.cursor()
    query =("insert into gs.products"
            "(name,uom_id,Price_per_unit)"
            "values(%s, %s, %s)")
    data =(products['Product_name'], products['uom_id'], products['Price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection,products_id):
    cursor = connection.cursor()
    query = ("Delete from products where products_id="+str(products_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,17))