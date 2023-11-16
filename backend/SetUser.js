import { View, Text } from 'react-native'
import React from 'react'
import { Constants } from 'expo-constants';
const SetUser = (Nombre, Apellidos, Correo, password, Tipo_Usuario) => {
  const Url = "http://192.168.100.61:5000";
  const register = `${Url}/CrteData?username=`+Nombre+
  '&apellidos='+Apellidos+
  '&Email='+Correo+
  '&Password='+password+
  '&tipo='+Tipo_Usuario;
// Realizar una solicitud HTTP (fetch) a la URL de registro
  return fetch(register)
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error en la solicitud');
    }
    return response.json();
  })

};

export default SetUser;
