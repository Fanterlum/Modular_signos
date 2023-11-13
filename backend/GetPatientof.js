import { View, Text } from 'react-native'
import React, { useEffect, useState } from 'react'
//Obtenemos el paciente consultando el ID del paciente
//Hace falta ver como se almacenara en la base de datos
//En el backend hacer una consulta por ID de doctor para obtener un json
//Con todos sus pacientes a su cuidado
const GetPatientof = async({ cedula }) => {
  console.log(cedula)
  const register = 'http://10.214.147.129:5000/drPatient?cedulaDoc=' +cedula;
  try {
    const response = await fetch(register);
    const jsonData = await response.json();
    return jsonData;
  } catch (error) {
    console.error("Error al realizar la solicitud:", error);
    throw error; // Puedes manejar el error de acuerdo a tus necesidades
  }
    };


export default GetPatientof