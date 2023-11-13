import { View, Text } from 'react-native'
import React from 'react'

const SetDoctor = (Nombre, Apellidos, Correo, password, Tipo_Usuario) => {
    const register = 'http://10.214.147.129:5000/CrteData?username='+Nombre+
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

export default SetDoctor