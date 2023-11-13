import { View, Text } from 'react-native'
import React from 'react'

const TextAssigner = ({ numero }) => {
    const obtenerTexto = (numero) => {
      if (numero == 0) {
        return 'Grave'; // Estado negativo, color rojo
      } else if (numero === 1) {
        return 'Irregular'; // Estado igual a 1, color naranja
      } else if (numero == 2) {
        return 'Estable'; // Estado positivo, color verde
      }
    };

    return obtenerTexto(numero);
  };

export default TextAssigner