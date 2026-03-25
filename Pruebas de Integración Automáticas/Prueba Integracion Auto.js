import http from 'k6/http';
import { check, sleep } from 'k6';

// CONFIGURACION
export const options = {
  vus: 5,
  duration: '10s',
};

// VARIABLES GLOBALES
const BASE_URL = 'https://reqres.in/api';

// FUNCION PRINCIPAL
export default function () {
  
  // AUTENTICACION
  const loginPayload = JSON.stringify({
    email: 'eve.holt@reqres.in',
    password: 'cityslicka'
  });

  const loginParams = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const loginResponse = http.post(`${BASE_URL}/login`, loginPayload, loginParams);

  check(loginResponse, {
    'El codigo de estado de Login es 200': (r) => r.status === 200,
    'La respuesta contiene un token': (r) => r.json('token') !== undefined,
  });

  const authToken = loginResponse.json('token');

  // OBTENCION DE PERFIL
  const profileParams = {
    headers: {
      'Authorization': `Bearer ${authToken}`,
      'Content-Type': 'application/json',
    },
  };

  const profileResponse = http.get(`${BASE_URL}/users/2`, profileParams);

  check(profileResponse, {
    'El codigo de estado del Perfil es 200': (r) => r.status === 200,
    'Los datos del usuario coinciden': (r) => r.json('data.id') === 2,
  });

  sleep(1);
}