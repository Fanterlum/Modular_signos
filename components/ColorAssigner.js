import { View, Text } from 'react-native'
import React from 'react'

const ColorAssigner = ({ numero }) => {
    const obtenerColorYTexto = (numero) => {
      if (numero == 0) {
        return { color: '#FA3A3A', texto: 'Grave' }; // Estado negativo, color rojo
      } else if (numero === 1) {
        return { color: '#FA9917', texto: 'Irregular' }; // Estado igual a 1, color naranja
      } else if (numero == 2) {
        return { color: '#97CC04', texto: 'Estable' }; // Estado positivo, color verde
      }
    };
    const { color, texto } = obtenerColorYTexto(numero);
    console.log('Color:', color);
    console.log('Texto:', texto);
    return { color, texto };
  };

export default ColorAssigner