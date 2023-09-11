import { StyleSheet, Text, View, Image } from 'react-native';
import React, { useState } from 'react';

//Asignador de color para el estado del paciente
import ColorAssigner from '../components/ColorAssigner';

const Patient_Info = () => {
  const [nombre, setNombre] = useState('Vicente'); // Variable para el nombre
  const [apellido, setApellido] = useState('Gonzalez Garcia'); // Variable para el apellido
  const [edad, setEdad] = useState('22'); // Variable para la edad
  //Aqui van los estados del paciente
  const [ActualState, setActualState] = useState(2); //ESTADO ACTUAL
  const [FutureState, setFutureStare] = useState(1); //Estado futuro
  //Aqui se piden los colores para cada estado
  const { colorActual, textoActual } = ColorAssigner({ numero: ActualState });
  const { colorFuture, textoFuture} = ColorAssigner({ numero: FutureState });
  //Aqui va la ruta o la peticion a la imagen del paciente
  const imageUrl = require('../assets/Sample/Patient.jpeg');

  console.log(colorActual);
  console.log(textoActual);

  return (
    <View style={styles.MainContainer}>
      <View style={styles.photoContainer}>
        <Text style={styles.titleText}>Datos del paciente:</Text>
        <Image source={imageUrl} style={styles.PatientPhoto}/>
      </View>
      <View style={styles.infoContainer}>
        <Text style={styles.DataText}>Nombre: {nombre}</Text>
        <Text style={styles.DataText}>Apellido: {apellido}</Text>
        <Text style={styles.DataText}>Edad: {edad}</Text>
      </View>
      <View style={styles.Patient_StatusContainer}>
      <View style={[styles.estados, { backgroundColor: colorActual }]}>
        <Text >Status Actual: {textoActual}</Text>
      </View>
      <View style={[styles.estados, { backgroundColor: colorFuture }]}>
        <Text >Status Futuro: {textoFuture}</Text>
      </View>
      </View>
      <View style={styles.chatbotContainer}>
        <Text>Aqui va el icono del chatbot</Text>
      </View>
    </View>
  )
}

export default Patient_Info

const styles = StyleSheet.create({
  estados: {
    width: "60%",
    height: "30%",
    marginLeft: "20%",
    borderRadius: 15,
    marginTop: "3%",
    alignItems: 'center',
    justifyContent: 'center',
  },
  titleText: {
    fontSize: 24,
    marginBottom: "3%",
    marginTop: "2%",
  },
  PatientPhoto: {
    width: "50%",
    height: "85%",

  },
  DataText: {
    marginTop: "5%",
    fontSize: 24,
  },
  MainContainer: {
    width: "100%",
    height: "100%",
    backgroundColor: "white",
  },
  photoContainer: {
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'top',
    width: "100%",
    height: "35%",
    flexDirection: "column",
  },
  infoContainer: {
    width: "100%",
    height: "30%",
    backgroundColor: "white",
    alignItems: 'center',
    justifyContent: 'top',
    flexDirection: "column",
  },
  Patient_StatusContainer: {
    width: "100%",
    height: "25%",
    backgroundColor: "yellow",
  },
  chatbotContainer: {
    width: "100%",
    height: "10%",
    backgroundColor: "red",
  },

});
