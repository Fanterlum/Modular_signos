import { View, Text } from 'react-native'
import React from 'react'

const GetGraph = async(id) => {
  const register = 'http://10.214.147.129:5000/signal?id=' + id;
  try {
    const response = await fetch(register);
    const jsonData = await response.json();
    return jsonData;
  } catch (error) {
    console.error("Error al realizar la solicitud:", error);
    throw error; // Puedes manejar el error de acuerdo a tus necesidades
  }
    };

export default GetGraph