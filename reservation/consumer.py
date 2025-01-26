# consumer.py
import pika

def main():
    # Connexion à RabbitMQ avec les informations d'identification
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq',  # L'hôte RabbitMQ dans le réseau Docker
            credentials=pika.PlainCredentials('admin', 'admin')  # Utilisation des informations d'identification
        )
    )
    channel = connection.channel()

    # Déclare une queue
    channel.queue_declare(queue='task_queue', durable=True)

    # Consommation des messages
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

