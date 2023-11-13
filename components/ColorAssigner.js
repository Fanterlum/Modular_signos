import { View, Text } from 'react-native'
import React from 'react'

const ColorAssigner = ({ numero }) => {
    const obtenerColor = (numero) => {
      if (numero == 0) {
        return '#FA3A3A'; // Estado negativo, color rojo
      } else if (numero === 1) {
        return '#FA9917'; // Estado igual a 1, color naranja
      } else if (numero == 2) {
        return '#97CC04'; // Estado positivo, color verde
      }
    };

    return obtenerColor(numero);
  };

export default ColorAssigner