import { View, Text } from 'react-native'
import React from 'react'
import axios from 'axios';
import Constants from 'expo-constants';

const Logged2 = async(Correo,password) => {
  const Url = "http://192.168.100.61:5000";

  const register = `${Url}/BackLogin?email=` + Correo + '&Password=' + password;
    try {
      const response = await fetch(register);
      const jsonData = await response.json();
      return jsonData;
    } catch (error) {
      console.error("Error al realizar la solicitud:", error);
      throw error; // Puedes manejar el error de acuerdo a tus necesidades
    }
  };
export default Logged2