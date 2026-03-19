import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '5s', target: 5 },
        { duration: '10s', target: 5 },
        { duration: '5s', target: 0 }
    ]
};

export default function () {
    const urlBase = 'https://jsonplaceholder.typicode.com';
    
    const parametrosPeticion = {
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        }
    };

    const cargaUtilPublicacion = JSON.stringify({
        title: 'Prueba de Carga k6',
        body: 'Evaluacion de transacciones continuas.',
        userId: 1
    });

    const respuestaPublicacion = http.post(`${urlBase}/posts`, cargaUtilPublicacion, parametrosPeticion);

    check(respuestaPublicacion, {
        'La creacion del contenido es exitosa (201)': (r) => r.status === 201,
        'La respuesta incluye un identificador valido': (r) => JSON.parse(r.body).hasOwnProperty('id')
    });

    const identificadorPublicacion = JSON.parse(respuestaPublicacion.body).id;

    const cargaUtilComentario = JSON.stringify({
        postId: identificadorPublicacion,
        name: 'Usuario Verificador',
        email: 'verificador@sistema.com',
        body: 'Comentario de prueba de integracion'
    });

    const respuestaComentario = http.post(`${urlBase}/comments`, cargaUtilComentario, parametrosPeticion);

    check(respuestaComentario, {
        'El comentario fue vinculado y creado exitosamente (201)': (r) => r.status === 201
    });

    sleep(1);
}