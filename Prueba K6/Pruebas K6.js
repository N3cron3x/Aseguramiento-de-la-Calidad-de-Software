import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '15s', target: 10 },
        { duration: '30s', target: 20 },
        { duration: '15s', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<1500'],
        http_req_failed: ['rate<0.01'],
    },
};

export default function () {
    const baseUrl = 'https://jsonplaceholder.typicode.com';

    const respuestaPosts = http.get(`${baseUrl}/posts`);
    check(respuestaPosts, {
        'Estado peticion general 200': (r) => r.status === 200,
        'Tiempo respuesta menor a 1500ms': (r) => r.timings.duration < 1500,
    });
    
    sleep(1);

    const respuestaPostIndividual = http.get(`${baseUrl}/posts/1`);
    check(respuestaPostIndividual, {
        'Estado articulo individual 200': (r) => r.status === 200,
    });
    
    sleep(1);
}