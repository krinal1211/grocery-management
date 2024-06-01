from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection,order):
    cursor=connection.cursor()
    order_query=("INSERT INTO orders"
                 "(customer_name,total,datetime) "
                 "VALUES (%s,%s,%s)")
    order_data=(order['customer_name'],order['grand_total'],datetime.now())
    cursor.execute(order_query,order_data)
    order_id=cursor.lastrowid

    order_detail_query=("INSERT INTO order_details "
                        "(order_id, product_id,quantity,total_price)"
                        "VALUES(%s, %s, %s, %s)")
    order_detail_data=[]
    for order_detail_record in order['order_details']:
        order_detail_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_detail_query,order_detail_data)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor=connection.cursor()
    query=("SELECT * FROM orders")
    cursor.execute(query)

    response=[]
    for (order_id,customer_name,total,datetime) in cursor:
        response.append(
            {
                'order_id':order_id,
                'customer_name':customer_name,
                'total':total,
                'datetime':datetime
            }
        )
    return response


if __name__=='__main__':
    connection=get_sql_connection()
    print(get_all_orders(connection))