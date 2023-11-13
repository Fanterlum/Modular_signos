import { View, Text } from 'react-native'
import React from 'react'
import axios from 'axios';
const Logged2 = async(Correo,password) => {
    const register = 'http://10.214.147.129:5000/BackLogin?email=' + Correo + '&Password=' + password;
    try {
      const response = await fetch(register);
      const jsonData = await response.json();
      return jsonData;
    } catch (error) {
      console.error("Error al realizar la solicitud:", error);
      throw error; // Puedes manejar el error de acuerdo a tus necesidades
    }
    /*
    const register = 'http://192.168.3.160:5000/BackLogin?email='+Correo+
    '&Password='+password;
  // Realizar una solicitud HTTP (fetch) a la URL de registro
    fetch(register)
    .then(response => response.json())
    .then(jsonData => {
        console.log("id:");
        console.log(jsonData.id);
        return jsonData;
        })
        */
    /*
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error en la solicitud');
      }
      console.log('Respuesta JSON:', response);
      return response.json();
    })
    */
  };
export default Logged2