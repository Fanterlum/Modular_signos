import { View, Text } from 'react-native'
import React from 'react'
import { Constants } from 'expo-constants';
const GetPromGraph = async(id) => {
  const Url = "http://192.168.100.61:5000";
  const register = `${Url}/signal?id=` + id;
  try {
    const response = await fetch(register);
    const jsonData = await response.json();
    return jsonData;
  } catch (error) {
    console.error("Error al realizar la solicitud:", error);
    throw error; // Puedes manejar el error de acuerdo a tus necesidades
  }
    };

export default GetPromGraph