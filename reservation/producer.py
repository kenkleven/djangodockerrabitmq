# producer.py
import pika
import sys

def send_message(message):
    # Connexion à RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq',  # L'hôte RabbitMQ dans le réseau Docker
            credentials=pika.PlainCredentials('admin', 'admin')  # Utilisation des informations d'identification
        )
    )
    channel = connection.channel()

    # Déclare une queue
    channel.queue_declare(queue='task_queue', durable=True)

    # Envoi du message à la queue
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Rendre le message persistant
        ))

    print(f" [x] Sent '{message}'")
    connection.close()

