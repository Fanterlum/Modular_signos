import { StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';
import React, { useEffect, useState } from 'react';
import Bot_Photo from '../components/items/Bot_Photo';

//Asignador de color para el estado del paciente
import ColorAssigner from '../components/ColorAssigner';
import TextAssigner from '../components/TextAssigner';

//Los estilos del paciente
import { styles } from '../Styles/Patient-Doctor/styles'; // Ajusta la ruta según la ubicación del archivo
//Se importa el chatbot
import ButtonChatbox from "../Chatbot/Components/ButtonChatbox";
/*
  Requerimientos al backend
  en el caso de acceder mediante el drawer, mandar como prop el id del paciente logeado
  en caso de venir desde Patient_List.js, se hace el paso del prop desde ahi
  Se hace una consulta con el ID del paciente y se muestra aqui toda su informacion en los useState
*/
const Patient_Info = ({navigation}) => {
  const [nombre, setNombre] = useState('Jennifer'); // Variable para el nombre
  const [apellido, setApellido] = useState('Hernandez Garcia'); // Variable para el apellido
  const [edad, setEdad] = useState('22'); // Variable para la edad
  const [Doctor, setDoctor] = useState('Vicente Gonzalez'); // Variable para la edad

  //Aqui van los estados del paciente
  const [ActualState, setActualState] = useState(1); //ESTADO ACTUAL
  const [FutureState, setFutureStare] = useState(2); //Estado futuro

  //Aqui va la ruta o la peticion a la imagen del paciente
  const imageUrl = require('../assets/Sample/Patient.jpeg');
  const navigateToStatistics = () => {
    navigation.navigate('Estadistica');
  };
  const navigateToHistory = () => {
    navigation.navigate('History');
  };
  return (
    <View style={styles.MainContainer}>
      <View style={styles.photoContainer}>
        <Text style={styles.titleText}>Datos del paciente:</Text>
        <Image source={imageUrl} style={styles.PatientPhoto}
                resizeMode="contain" // Controla cómo se ajusta la imagen
                />
      </View>
      <View style={styles.infoContainer}>
        <Text style={styles.DataText2}>Nombre: {nombre}</Text>
        <Text style={styles.DataText}>Apellido: {apellido}</Text>
        <Text style={styles.DataText}>Edad: {edad}</Text>
        <Text style={styles.DataText}>Doctor a cargo: {Doctor}</Text>

      </View>
      <View style={styles.Patient_StatusContainer}>
      <View style={[styles.estados, { backgroundColor: ColorAssigner({ numero: ActualState }) }]}>
        <Text style={styles.StatusText}>Status Actual: {TextAssigner({ numero: ActualState })}</Text>
      </View>
      <View style={[styles.estados, { backgroundColor: ColorAssigner({ numero: FutureState }) }]}>
        <Text style={styles.StatusText}>Status Futuro: {TextAssigner({ numero: FutureState })}</Text>
      </View>
      </View>
      <View style={styles.botContainer}>
        {/* botContainer se superpondrá sobre los demás elementos */}
        <View style={styles.buttonChatboxContainer}>
          {/* ButtonChatbox se posicionará en la mitad de la pantalla */}
          <ButtonChatbox></ButtonChatbox>
        </View>
      </View>
    </View>
  )
}

export default Patient_Info