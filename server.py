from cgi import print_arguments
import socket
import ssl
import conectionDB

rows = conectionDB.connecion()

usuarios = {}
cont = 1
body = ''
for row in rows:
    usuarios['row_' + str(cont)] = {'person_id': row[0],
                        'firstName': row[1],
                        'lastName': row[2],
                        'address': row[3]}
    body += '<div style="border: 3px solid black; background-color: red; color: white; margin: 4px 0;">' + 'IdPersona: ' + str(row[0]) + ' | firstName:' + row[1] + ' | lastName:' + row[2] + ' | adress:' + row[3] + '</div>'
    cont+=1

#print(usuarios)

def iniciarServidor(host, puerto):

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #context.load_cert_chain('./domain.crt')
    context.load_verify_locations('./domain.crt')

    sck_bind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck_bind.bind((host, puerto))
    sck_bind.listen(4)

    while True:
        
        (new_socket, addr_client) = sck_bind.accept()
        conn_ssl = context.wrap_socket(new_socket , server_side=True)

        print(conn_ssl.cipher())

        print("Se estableció conexión con: %s" % str(addr_client))
        
        print("Se estableció conexión con: %s" % str(addr_client))
        msg = '<!DOCTYPE html> <html> <head> <meta charset="UTF-8">  <title>Ejemplo servidor HTML</title> </head>' + body + '<body></body> </html>'
        new_socket.send(msg.encode('utf8'))
        msg_rec = new_socket.recv(1024)

        print(msg_rec.decode('utf-8'))
    
        new_socket.close()

if __name__ == "__main__":
    host="localhost"
    puerto = 80
    iniciarServidor(host, puerto)